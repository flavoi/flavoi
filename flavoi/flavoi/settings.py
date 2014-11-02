"""
Django settings for flavoi project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from unipath import Path
import json

BASE_DIR = Path(__file__).ancestor(2)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
from django.core.exceptions import ImproperlyConfigured

# JSON-based secrets module
with open(BASE_DIR.child('secrets.json'), 'r') as f:
    secrets = json.load(f)

def get_secret(settings, secrets=secrets):
    """Get the secret variable or return explicit exception."""
    try:
        return secrets[settings]
    except KeyError:
        error_msg = "Set the {0} enviroment variable".format(settings)
        raise ImproperlyConfigured(error_msg)

# Configuration vars
# SECURITY WARNING: keep the secret keys used in production secret!

SECRET_KEY = get_secret('FLAVOI_KEY')

CURRENT_PROFILE = get_secret('CURRENT_PROFILE')

ALLOWED_HOSTS = []

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

TEMPLATE_DEBUG = True

# Applications
# https://docs.djangoproject.com/en/1.7/ref/applications/

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'storages',
)

LOCAL_APPS = (
    'bio',
    'goal',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'flavoi.urls'

WSGI_APPLICATION = 'flavoi.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'bio.context.copyright',
    'bio.context.profile',
)

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR.child('flavoi.db'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/topics/i18n/

# Amazon S3 support
# http://aws.amazon.com/

# CKEditor support
# https://github.com/shaunsephton/django-ckeditor

AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = get_secret('AWS_STORAGE_BUCKET_NAME')

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
DEFAULT_S3_PATH = 'media'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATIC_S3_PATH = 'static'

MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
MEDIA_URL = '//s3.amazonaws.com/%s/media/' % AWS_STORAGE_BUCKET_NAME
STATIC_ROOT = "/%s/" % STATIC_S3_PATH
STATIC_URL = '//s3.amazonaws.com/%s/static/' % AWS_STORAGE_BUCKET_NAME
ADMIN_MEDIA_PREFIX = 'admin/'