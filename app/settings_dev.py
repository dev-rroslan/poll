from .base import *

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