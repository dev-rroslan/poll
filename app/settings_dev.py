from .base import *
import os
from dotenv import load_dotenv # type: ignore
os.getenv('RESEND')

ALLOWED_HOST = ['http://127.0.0.1:8000']

DEBUG=True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_DEV_NAME'),
        'USER': os.getenv('DB_DEV_USER'),
        'PASSWORD': os.getenv('DB_DEV_PASSWORD'),
        'HOST': os.getenv('DB_DEV_HOST'),
        'PORT': os.getenv('DB_DEV_PORT'),
    }
}   
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False