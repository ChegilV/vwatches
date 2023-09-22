from puddle.settings import *
from decouple import config


SECRETE_KEY = config('SECRETE_KEY')
ALLOWED_HOSTS = ['web-production-8000.up.railway.app']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASSWORD'),
        'HOST': config('DATABASE_HOST'),
        'PORT': config('DATABASE_PORT'),
    }
}