# -*- coding: utf-8 -*-

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG


ADMINS = (
   # ('leona', 'jin.leona@gmail.com'),
)

DATABASES = {
    'default': {
        'ENGINE': 'mysql',
        'NAME': 'ppy_ios_one',
        'USER': 'root',
        'PASSWORD': 'mysql_pwd',
        'HOST': 'localhost',
        'PORT': '3306',
    },
    'second': {
        'ENGINE': 'mysql',
        'NAME': 'ppy',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': ''
    },
    'third': {
        'ENGINE': 'mysql',
        'NAME': 'ppy',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': '',
    }
}


TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1
SITE_URL = 'http://iphone.raytoon.com'
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
SITE_PROJECT_NAME = os.path.basename(SITE_ROOT)

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True


MEDIA_ROOT = '/usr/local/nginx/html/ios/ppy_media/'
MEDIA_URL = 'http://iphone.raytoon.com/ppy_media/'
ADMIN_MEDIA_PREFIX = 'http://iphone.raytoon.com/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2k4aa7q-tqr@!%m*4da2p2@9qzg=-4lr7)w(b2!yh1zvaq_=9&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.csrf',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    #'django.middleware.csrf.CsrfResponseMiddleware',
    'amf.django.middleware.AMFMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, 'templates'),
    #'E:/workspace/bubblefish/ppy_official/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.flatpages',
    'apps',
)


CACHE_BACKEND = 'django_pylibmc.memcached://127.0.0.1:11311/?timeout=86400'

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

# SMTP SERVER{{{
EMAIL_HOST = ''
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 25


LOGIN_URL = '/users/login/'
LOGOUT_URL = '/users/logout/'

