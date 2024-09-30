from pathlib import Path
import os
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-6+(k0auu+8_b&@)s)5hujfrj0bp@lf-5a+#eh_qs#h*a$gqz&o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["0.0.0.0", "localhost"]

AUTH_USER_MODEL = 'rapihogar.User'
# Application definition

INSTALLED_APPS = [
    # Core Django apps that provide essential functionality:
    'django.contrib.admin',         # Django's admin interface
    'django.contrib.auth',          # Authentication system for users
    'django.contrib.contenttypes',  # Handles content types in models
    'django.contrib.sessions',      # Session management for storing user sessions
    'django.contrib.messages',      # Framework for temporary messages in views
    'django.contrib.staticfiles',   # Manages static files like CSS and JavaScript

    # Third-party apps:
    'rest_framework.authtoken',     # Token-based authentication for Django Rest Framework (DRF)
    'django_extensions',            # Extra management commands and extensions for Django
    'rest_framework',               # Main Django Rest Framework (DRF) app for building APIs
    'drf_yasg',                     # A tool for generating Swagger/OpenAPI documentation for DRF APIs
    'django_filters',               # Provides filter functionality for REST APIs

    # Custom apps in the project:
    'rapihogar',                    # Main custom app for your Rapihogar project
    'api',                          # Separate app for handling the API logic (if needed)
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

ROOT_URLCONF = 'rapihogar.urls'

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

WSGI_APPLICATION = 'rapihogar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases
load_dotenv()
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DB_ENGINE', default='django.db.backends.sqlite3'),
        'NAME':  os.getenv('DB_NAME', default=BASE_DIR / 'db.sqlite3'),
        'USER': os.getenv('DB_USER', default=''),
        'PASSWORD': os.getenv('DB_PASSWORD', default=''),
        'HOST': os.getenv('DB_HOST', default='localhost'),
        'PORT': os.getenv('DB_PORT', default='5432'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    # Renderer classes to define how API responses are rendered:
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',           # Renders responses as JSON (most common for APIs)
        'rest_framework.renderers.BrowsableAPIRenderer',   # Provides a web-browsable API interface for testing
    ),

    # Enables filtering in API views by specifying filter backends:
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],

    # Schema generation for automatic OpenAPI/Swagger documentation using DRF Spectacular:
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
