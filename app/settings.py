from .base import *
import os
from dotenv import load_dotenv # type: ignore
os.getenv('RESEND')
DEBUG = False
ALLOWED_HOSTS = ['poll.applikasi.tech', '165.154.236.48', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://poll.applikasi.tech']


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SECURE_SSL_REDIRECT = False
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
