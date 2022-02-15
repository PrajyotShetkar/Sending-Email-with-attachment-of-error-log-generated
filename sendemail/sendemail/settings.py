"""
Django settings for sendemail project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
import logging
from os.path import dirname

BASE_DIR = dirname(dirname(dirname(dirname(os.path.abspath(__file__)))))

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.utils.log import DEFAULT_LOGGING

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-b7f+sipm32lgj^y_y+z*nhz80^5(8=!iy7@vk!6w8t+6e-aa&-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'myapp',
]

MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sendemail.urls'

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

WSGI_APPLICATION = 'sendemail.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
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

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

CONTENT_DIR = os.path.join(BASE_DIR, 'content')


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
ADMINS = [('Me', 'prajyotps@datatemplate.com'), ]
MANAGERS = ADMINS
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'Prajyot Shetkar <prajyotps@datatemplate.com>'
SERVER_EMAIL = 'django@my-domain.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'prajyotps@datatemplate.com'
EMAIL_HOST_PASSWORD = 'ScaryHell@123'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FILE_PATH = '..\media\logg.txt'

DEFAULT_LOGGING['handlers']['console']['filters'] = []
LOGGING_CONFIG = None
LOGGING_CONFIG = None
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': '{levelname} {asctime} {module} '
			          '{process:d} {thread:d} {message}',
			'style': '{',
		},
		'simple': {
			'format': '{levelname} {message}',
			'style': '{',
		},
	},
	'handlers': {
		'console': {
			'level': 'INFO',
			'class': 'logging.StreamHandler',
			'formatter': 'simple'
		},
		'file': {
			'level': 'INFO',
			'class': 'logging.handlers.RotatingFileHandler',
			'filename': 'logg.txt',
			'maxBytes': 1024 * 1024 * 10,  # 10MB
			'backupCount': 10,
			'formatter': 'verbose'
		},
	},
	'loggers': {
		'': {
			'level': 'INFO',
			'handlers': ['console', 'file'],
		},
		'django': {
			'handlers': ['console', 'file'],
			'level': 'ERROR',
			'propagate': False,
		},
		'django.db.backends': {
			'handlers': ['console', 'file'],
			'level': 'ERROR',
			'propagate': False,
		},
		'django.server': {
			'handlers': ['console', 'file'],
			'level': 'INFO',
			'propagate': False,
		}
	}
}

logging.config.dictConfig(LOGGING)
logger = logging.getLogger(__name__)
logger.info('Logging works!')
