from .defaults import *
from decouple import config

DEBUG = False

ALLOWED_HOSTS = ['159.65.156.67']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("DB_NAME"),
        'USER': config("DB_USER"),
        'PASSWORD': config("DB_USER_PASS"),
        'HOST': 'localhost',
        'PORT': '',
    }
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

