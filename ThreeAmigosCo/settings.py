"""
Django settings for ThreeAmigosCo project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-gvg0@ze%bctsf8jx@v62=&#5tmsjk##1ki%vuww#ko+=zp5djz"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "jazzmin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third Party
    'taggit',
    'ckeditor',

    # Pament Integration
    'paypal.standard.ipn',
  

    # Custom Apps
    'core',
    'userauths',
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "ThreeAmigosCo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "core.context_processor.default",
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "ThreeAmigosCo.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"



JAZZMIN_SETTINGS = {
    'site_header' : "3AmigosCo shop",
    'site_brand' : "You order, we deliver",
    'site_logo' : "assets/imgs/theme/loading.gif",
    'copyright': "ThreeAmigosCorp-store.com",
}


LOGIN_URL = "userauths:sign-in"



AUTH_USER_MODEL = 'userauths.User'

CKEDITOR_UPLOAD_PATH = 'uploads/'


CKEDITOR_CONFIGS = {
    "default": {
        
        "skin": "moono",
        "codeSnippet_theme": "monokai",
        "toolbar": "all",
        "extraPlugins": ",".join(
            [
                "codesnippet",
                "widget",
                "dialog"
            ]
        ),
        
    
    }
}

# # PayPal Sandbox API credentials
# PAYPAL_CLIENT_ID = 'Ad4EKlA_HUOoFxasIZ7N0f683wnnjpQf62vlRhsz2iRcfeMWGiV6-jiPMVGDihf1yLtxsjLoH7R4AInE'
# PAYPAL_SECRET = 'ENjjTzoUj3GrvMC0E_gys5n9Y_qbQtRGMPgrOHHzDrw9CmSGfIhQh30_z-EUP2IsbvdI5MbEqR2VrQtQ'

PAYPAL_RECEIVER_EMAIL = 'sb-kmfou29400057@business.example.com'
PAYPAL_TEST = True