# -*- encoding: utf-8 -*-
"""
Django settings for seanpanama project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# Base dir local, para uso local
#import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))


#Base dir para uso en heroku
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'f36cdq%0$8uswe4jl84m#@0@8uv(2*m@e71ur64@sgdt@hr@o-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

#Host permitidos para instalacion local
#ALLOWED_HOSTS = []
#Host permitidas para heroku
ALLOWED_HOSTS = ['seanpanama.herokuapp.com']


# Redirect when login is correct.
LOGIN_REDIRECT_URL = "/tutores"
# Redirect when login is not correct.
LOGIN_URL = '/login'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sean',
    'tutores',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'seanpanama.urls'

WSGI_APPLICATION = 'seanpanama.wsgi.application'

#MEDIA_ROOT = os.path.join(BASE_DIR,'sean/static/img')
MEDIA_ROOT = 'https://googledrive.com/host/0BxRrY6bltzTGfnlIaUJiYmc0MU82MmtKNEFibG85b1dBMVQ4RF9ndzlkMzVqeEJ5M3ZqMmM/img'

MEDIA_URL = '/media/'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': 'seanpanama.db3',
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

#STATIC_ROOT = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-2] + ['static'])

#STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.CachedStaticFilesStorage'

#STATIC_URL = '/static/'

#Administrador
ADMINS = (
    ('Alonso Ugalde Aguilar', 'augaldecr@gmail.com'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS = TEMPLATE_CONTEXT_PROCESSORS + (
    'sean.context_processors.versiculo',
    'sean.context_processors.menu',
    'sean.context_processors.ultimas_noticias',
)

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
#ALLOWED_HOSTS = ['*']

# Static asset configuration

STATIC_ROOT = 'staticfiles'
STATIC_URL = 'https://googledrive.com/host/0BxRrY6bltzTGfnlIaUJiYmc0MU82MmtKNEFibG85b1dBMVQ4RF9ndzlkMzVqeEJ5M3ZqMmM/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '/static/'),
#    'https://googledrive.com/host/0BxRrY6bltzTGfnlIaUJiYmc0MU82MmtKNEFibG85b1dBMVQ4RF9ndzlkMzVqeEJ5M3ZqMmM',
)