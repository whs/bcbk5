"""
Django settings for bcbk5 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import socket
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '26d6(i0jvg^nuf!#u*bcr&sy(bw6ps846%$8j0yjcgpa=jwe5('

# SECURITY WARNING: don't run with debug turned on in production!
IS_PROD = socket.gethostname() == 'madoka'
DEBUG = not IS_PROD
TEMPLATE_DEBUG = not IS_PROD

ALLOWED_HOSTS = [
    'api.2014.barcampbangkhen.org'
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_docs',
    'corsheaders',
    'registration',
    'schedule'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'bcbk5.urls'

WSGI_APPLICATION = 'bcbk5.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = True

USE_ETAGS = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'DEFAULT_THROTTLE_CLASSES': (
        'registration.throttle.PostScopedRateThrottle',
    ),
    'DEFAULT_THROTTLE_RATES': {
        'regis': '1/minute',
    }
}

DEFAULT_FROM_EMAIL = 'Barcamp Bangkhen <barcamp@barcampbangkhen.org>'
PUSH_PUBLISH = ''
X_FRAME_OPTIONS = 'DENY'

CORS_ORIGIN_ALLOW_ALL = DEBUG

CORS_ORIGIN_WHITELIST = (
    'localhost',
    '2014.barcampbangkhen.org'
)

REGIS_OPEN = True

try:
    from site_settings import *
except ImportError:
    pass
