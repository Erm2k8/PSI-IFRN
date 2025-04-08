from django.http import HttpResponse

def my_view(request):
    return HttpResponse("<h1>HOLA MUNDITO</h1>")