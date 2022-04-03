from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'incidentes',
        'USER':'root',
        'PASSWORD':'root',
        'HOST':'127.0.0.1',
        'POST':3306
    }
}


STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR.child('static')]

STATIC_ROOT = BASE_DIR.child('staticfiles')