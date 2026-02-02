from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from loja.forms.AuthForm import LoginForm, RegisterForm, RecoveryForm, ChangePasswordForm
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.conf import settings
from loja.models import Usuario
import hashlib
import time


def login_view(request):
    loginForm = LoginForm()
    message = None
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                _next = request.GET.get('next')
                if _next is not None:
                    return redirect(_next)
                else:
                    return redirect("/")
        else:
            message = {'type': 'danger', 'text': 'Dados de usuário incorretos'}
    context = {'form': loginForm, 'message': message,'title': 'Login', 'button_text': 'Entrar', 'link_text': 'Registrar', 'link_href': '/register'}
    return render(request, template_name='auth/auth.html', context=context, status=200)


def register_view(request):
    registerForm = RegisterForm()
    message = None
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            verifyUsername = User.objects.filter(username=username).first()
            verifyEmail = User.objects.filter(email=email).first()
            if verifyUsername is not None:
                message = { 'type': 'danger', 'text': 'Já existe um usuário com este username!' }
            elif verifyEmail is not None:
                message = { 'type': 'danger', 'text': 'Já existe um usuário com este e-mail!' }
            else:
                user = User.objects.create_user(username, email, password)
                if user is not None:
                    message = { 'type': 'success', 'text': 'Conta criada com sucesso!' }
                else:
                    message = { 'type': 'danger', 'text': 'Um erro ocorreu ao tentar criar o usuário.' }
    context = { 'form': registerForm, 'message': message,'title': 'Registrar', 'button_text': 'Registrar', 'link_text': 'Login', 'link_href': '/login' }
    return render(request, template_name='auth/auth.html', context=context, status=200)


def logout_view(request):
    logout(request)
    return redirect('/login')


def send_email(usuario):
    context = {'token': usuario.token}
    html_message = render_to_string('auth/recovery.html', context)
    plain_message = strip_tags(html_message)
    try:
        send_mail(
            subject="Recuperação de Senha",
            message=plain_message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[usuario.user.email],
            html_message=html_message,
            fail_silently=False,
        )
    except Exception as exc:
        # não propaga exceção de envio de e-mail em ambiente de desenvolvimento
        try:
            import logging
            logging.getLogger(__name__).exception('Erro ao enviar e-mail de recuperação: %s', exc)
        except Exception:
            pass
        return False

    return True


def recovery_view(request):
    context = {}
    if request.method == 'POST':
        form = RecoveryForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            usuario = Usuario.objects.filter(user__email=email).first()
            
            email_sent = False
            if usuario:
                token_hash = hashlib.sha256(str(time.time()).encode()).hexdigest()
                usuario.token = token_hash
                usuario.save()
                email_sent = send_email(usuario)

            if usuario and not email_sent:
                context['message'] = {
                    'type': 'danger', 
                    'text': 'Falha no envio: A rede pode estar bloqueando a conexão SMTP (Porta 587).'
                }
            else:
                context['message'] = {
                    'type': 'success', 
                    'text': 'Se o e-mail existir, um link de recuperação foi enviado.'
                }
    else:
        form = RecoveryForm()

    context['form'] = form
    context['title'] = 'Recuperação de Senha'
    context['button_text'] = 'Enviar'
    context['link_text'] = 'Login'
    context['link_href'] = '/login'
    return render(request, 'auth/auth.html', context)


def change_password(request, token):
    usuario = Usuario.objects.filter(token=token).first()
    if not usuario:
        return redirect('recovery')

    if request.method == 'POST':
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            user = usuario.user
            user.set_password(password)
            user.save()

            usuario.token = None
            usuario.save()
            return redirect('login')
    else:
        form = ChangePasswordForm()

    context = {'form': form, 'title': 'Alterar Senha', 'button_text': 'Alterar', 'link_text': 'Login', 'link_href': '/login'}
    return render(request, 'auth/auth.html', context)

