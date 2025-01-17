"""
Django settings for foolish_division project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "0.0.0.0",
    "127.0.0.1",
    "www.foolish-division.com",
    "api.foolish-division.com",
    "foolish-division.onrender.com",
    "foolish-division-frontend.onrender.com",
]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "django_browser_reload",
    "foolish_division.expenses",
    "foolish_division.log",
    "foolish_division.profiles",
    "foolish_division.expense_auth",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = "foolish_division.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "foolish_division.wsgi.application"


# Database
DB_NAME = os.getenv("DJANGO_DB_NAME", "foolish_db")
DB_USER = os.getenv("DJANGO_DB_USER", "foolish-user")
DB_PASSWORD = os.getenv("DJANGO_DB_PASSWORD", "foolish-pg-pass")
DB_HOST = os.getenv("DJANGO_DB_HOST", "postgres")
DB_PORT = os.getenv("DJANGO_DB_PORT", "5432")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'foolish_division.expense_auth.authentication.FoolishTokenAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': (
            'rest_framework.parsers.JSONParser',
            'rest_framework.parsers.FormParser',
            'rest_framework.parsers.MultiPartParser',
    ),
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.expense_auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.expense_auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.expense_auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.expense_auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",
    "https://www.foolish-division.com",
    "https://api.foolish-division.com",
    "https://foolish-division.onrender.com",
]

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "https://localhost",
    "https://www.foolish-division.com",
    "https://api.foolish-division.com",
    "https://foolish-division.onrender.com",
]

DJANGO_AUTH_TOKEN_MAX_AGE_SECONDS = int(os.getenv("DJANGO_AUTH_TOKEN_MAX_AGE_SECONDS", 300000))
