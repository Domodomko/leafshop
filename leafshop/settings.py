from pathlib import Path
import os
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'kab_2u%^#!b!v-*&1==u5&c%%@j^7lphd@=mi7sj644+_1$vlm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',
    'widget_tweaks',
    'ckeditor',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'leafshop.urls'

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

WSGI_APPLICATION = 'leafshop.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         #
#         'ENGINE': 'django.db.backends.postgresql',
#         #
#         'HOST': config('DB_HOST'),
#         'PORT': config('DB_PORT'),
#         'NAME': config('DB_DATABASE'),
#         'USER': config('DB_USERNAME'),
#         'PASSWORD': config('DB_PASSWORD'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = False

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATIC_DIR = os.path.join(BASE_DIR, 'static/shop')
STATICFILES_DIRS = [STATIC_DIR]

# Email settings
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_BACKEND = config('EMAIL_BACKEND')
CONTACT_US_EMAIL = config('CONTACT_US_EMAIL')

# Session settings
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_AGE = 2419200

# Ckeditor settings
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar': 'toolbar_YourCustomToolbarConfig',
        'toolbar_YourCustomToolbarConfig': [
            {'name': 'document', 'items': ['mode', 'document', 'doctools']},
            {'name': 'clipboard', 'items': ['clipboard', 'undo']},
            {'name': 'editing', 'items': ['find', 'selection', 'spellchecker', 'editing']},
            {'name': 'forms', 'items': ['forms']},
            '/',
            {'name': 'basicstyles', 'items': ['basicstyles', 'cleanup']},
            {'name': 'paragraph', 'items': ['list', 'indent', 'blocks', 'align', 'bidi', 'paragraph']},
            {'name': 'links', 'items': ['links']},
            {'name': 'insert', 'items': ['insert']},
            '/',
            {'name': 'styles', 'items': ['styles']},
            {'name': 'colors', 'items': ['colors']},
            {'name': 'tools', 'items': ['tools']},
            {'name': 'others', 'items': ['others']},
            {'name': 'about', 'items': ['about']}
        ]
    },
}

DEFAULT_AUTO_FIELD='django.db.models.AutoField'
