"""
Django settings for djangoproject project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
from os import path, getenv
from dotenv import load_dotenv
import sys
import cloudinary

config = cloudinary.config(secure=True)

import cloudinary.uploader
import cloudinary.api

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'djangogramm',
    'easy_thumbnails',
    'django_extensions',
    'bootstrap5',
    'django_bootstrap_icons',
    'debug_toolbar',
    'cloudinary',
    'social_django',
]

AUTH_USER_MODEL = 'djangogramm.User'

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'djangoproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangoproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# Local

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'databdjango',
#         'USER': 'dbuser',
#         'PASSWORD': 'dbpass',
#         'HOST': '127.0.0.1',
#         'PORT': 5433,
#     }
# }

# Heroku Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd3fli833kgo360',
        'USER': 'oodyhopwdfsuvt',
        'PASSWORD': getenv('HEROKU_POSTGRES_PASSWORD'),
        'HOST': 'ec2-54-91-223-99.compute-1.amazonaws.com',
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = 'anna.stbmag@gmail.com'
EMAIL_HOST_PASSWORD = getenv('EMAIL_HOST_PASSWORD')

AUTHENTICATION_BACKENDS = [
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.github.GithubOAuth2',
    'djangogramm.utils.EmailBackend',
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.social_auth.associate_by_email',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# GITHUB

SOCIAL_AUTH_GITHUB_KEY = 'b3fecdad6798e0d5971e'
SOCIAL_AUTH_GITHUB_SECRET = getenv('SOCIAL_AUTH_GITHUB_SECRET')
SOCIAL_AUTH_GITHUB_SCOPE = ['user:email']

# GOOGLE

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '440269591802-i6p5p4qm2h6c4hljd41a5q7v605jev0t.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_JSONFIELD_ENABLED = True

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LOGIN_URL = '/login/'

LOGIN_REDIRECT_URL = '/'

LOGOUT_REDIRECT_URL = '/login/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = path.join(BASE_DIR, 'djangogramm', 'static')

STATICFILES_DIRS = []

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Amazon S3
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

DEFAULT_USER_AVATAR = 'https://res.cloudinary.com/dsc8n66p9/image/upload/v1658503584/avatars/user_icon_msyg0x.png'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

INTERNAL_IPS = [
    "127.0.0.1",
]

# Heroku

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'annapronka',
    'API_KEY': '367934168612453',
    'API_SECRET': getenv('API_SECRET')
}

# Local

cloudinary.config(
    cloud_name="annapronka",
    api_key="443484951313792",
    api_secret=getenv('api_secret')
)

if 'test' in sys.argv:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase'
    }

import django_heroku
django_heroku.settings(locals(), staticfiles=False)