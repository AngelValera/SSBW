"""
Django settings for mi_sitio_web project.

Generated by 'django-admin startproject' using Django 2.2.10.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import socket
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@&sij5nk^n^5m4rg@zvjgknm23w2vcmw=+7hbv#0$-i+^)^r49'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']
CORS_ORIGIN_ALLOW_ALL = True

# Application definition

INSTALLED_APPS = [    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',  
    'visitas_granada.apps.VisitasGranadaConfig',
    'debug_toolbar',
    'sorl.thumbnail',
    'crispy_forms',
    'rest_framework',
    'corsheaders', 
]

MIDDLEWARE = [  
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',    
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'mi_sitio_web.urls'
TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_PATH],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',                
            ],
        },
    },
]

WSGI_APPLICATION = 'mi_sitio_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es-es'

TIME_ZONE = 'Europe/Madrid'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '/code/static/'
#STATIC_PATH = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS = (
#    STATIC_PATH,
#)

MEDIA_URL = '/media/'
MEDIA_ROOT = '/code/media/'

# -----------------------
# Para el debug toolbar en docker
# -----------------------
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + '1' for ip in ips] + ['127.0.0.1', '10.0.2.2']

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}
LOGIN_REDIRECT_URL = 'index'
LOGOUT_REDIRECT_URL = 'index'


LOG_FILE = 'visitas_granada.log'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s [%(name)s:%(lineno)s] %(message)s'
        },
    },

    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, LOG_FILE),
            'formatter': 'verbose',
            'mode': 'w'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        }
    },

    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'ERROR',
        },
        'visitas_granada': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
    }
}


