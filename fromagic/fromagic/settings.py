"""
Django settings for fromagic project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from oscar.defaults import *
from oscar import get_core_apps
from django.utils.translation import ugettext_lazy as _


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pq#h1h2bj!+$y*9rats)js8#*220lyl266hg)r@hl(_^rep_r*'

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
    'django.contrib.flatpages',
    'django.contrib.sites',
    'compressor',
    'widget_tweaks',
] + get_core_apps()

SITE_ID = 1

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'fromagic.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.promotions.context_processors.promotions',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.customer.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]

WSGI_APPLICATION = 'fromagic.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'fromagic_db',
        'USER': 'fromagic_admin',
        'PASSWORD': 'pass',
        'HOST': '',
        'PORT': '',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/fromagic/static/'
MEDIA_URL = '/fromagic/media/'
THUMBNAIL_DEBUG = True
STATIC_ROOT = os.path.join(BASE_DIR, 'fromagic.static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'fromagic.media')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


# Oscar settings


HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine'
    }
}

OSCAR_INITIAL_ORDER_STATUS = 'Pending'
OSCAR_INITIAL_LINE_STATUS = 'Pending'
OSCAR_ORDER_STATUS_PIPELINE = {
    'Pending': ('Being processed', 'Cancelled',),
    'Being processed': ('Processed', 'Cancelled',),
    'Cancelled': (),
}

OSCAR_DASHBOARD_NAVIGATION = [
    {
        'label': _('Fromagic dashboard'),
        'icon': 'icon-th-list',
        'url_name': 'dashboard:index',
    },
    {
        'label': _('Shop'),
        'icon': 'icon-shopping-cart',
        'children': [
            {
                'label': _('Products'),
                'url_name': 'dashboard:catalogue-product-list',
            },
            {
                'label': _('Categories'),
                'url_name': 'dashboard:catalogue-category-list',
            },
        ]
    },
    {
        'label': _('Orders'),
        'icon': 'icon-line-chart',
        'children': [
            {
                'label': _('Order List'),
                'url_name': 'dashboard:order-list',
            },
            {
                'label': _('Order Statistics'),
                'url_name': 'dashboard:order-stats',
            },
        ]
    },
    {
        'label': _('Users'),
        'icon': 'icon-group',
        'url_name': 'dashboard:users-index',
    },
    {
        'label': _('Vouchers'),
        'icon': 'icon-bullhorn',
        'children': [
            {
                'label': _('Edit Vouchers'),
                'url_name': 'dashboard:voucher-list',
            },
            {
                'label': _('Product Ranges'),
                'url_name': 'dashboard:range-list',
            },
        ]
    },
    {
        'label': _('Featured Brands and other Content'),
        'icon': 'icon-folder-close',
        'children': [
            {
                'label': _('Content Blocks'),
                'url_name': 'dashboard:promotion-list',
            },
            {
                'label': _('Content Block Pages'),
                'url_name': 'dashboard:promotion-list-by-page',
            },
        ]
    },
]
