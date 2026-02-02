from .settings import*

# Carrega variáveis do arquivo .env e expõe erros/avisos no console
try:
    from dotenv import load_dotenv, find_dotenv
    loaded = load_dotenv(find_dotenv())
    if not loaded:
        print('Warning: .env file not found or could not be loaded.')
except Exception as exc:
    print('Error loading .env:', exc)

# Configurações de e-mail a partir do .env (úteis para desenvolvimento)
import os
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
try:
    EMAIL_PORT = int(os.environ.get('EMAIL_PORT', 587))
except Exception:
    EMAIL_PORT = 587
EMAIL_USE_TLS = str(os.environ.get('EMAIL_USE_TLS', 'True')).lower() in ('true', '1', 'yes')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL', EMAIL_HOST_USER)
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

# Aviso rápido se credenciais essenciais estiverem ausentes
missing_email = []
if not EMAIL_HOST_USER:
    missing_email.append('EMAIL_HOST_USER')
if not EMAIL_HOST_PASSWORD:
    missing_email.append('EMAIL_HOST_PASSWORD')
if missing_email:
    print('Warning: Missing email configuration variables:', ', '.join(missing_email))

DEBUG = True
SECRET_KEY='ixb62ha#ts=ab4t2u%p1_62-!5w2j==j6d^3-j$!z(@*m+-h'
DATABASES={
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}