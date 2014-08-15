#!/usr/bin/python
# -*- coding: utf-8 -*-
from spirit.settings import *
import os.path

DEBUG = True
TEMPLATE_DEBUG = DEBUG
HERE = os.path.dirname(os.path.abspath(__file__))
PARENT = os.path.split(HERE)[0]
ADMINS = (
    ('jason', 'admin@wingzen.com'),
)
MANAGERS = ADMINS



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'db_wz',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '831128',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['www.wingzen.com', 'wingzen.com','newdust.webfactional.com']

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
# Development MEDIA_ROOT
MEDIA_ROOT = os.path.join(HERE, 'media').replace('\\', '/')
# Production MEDIA_ROOT
#MEDIA_ROOT = '/home/newdust/webapps/media/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
# Development STATIC_ROOT
STATIC_ROOT = os.path.join(PARENT, 'static').replace('\\', '/')
# Production STATIC_ROOT
#STATIC_ROOT = '/home/newdust/webapps/static/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(HERE, 'static').replace('\\', '/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '118h35r92xad==%1s^w#4r4*@thfe6jh_(vb4*v81-h&amp;kfbq4v'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS += (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#   'django.template.loaders.eggs.Loader',
)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.debug',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.media',
#    'django.core.context_processors.request',
#)


MIDDLEWARE_CLASSES += (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    #'pagination.middleware.PaginationMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
)


ROOT_URLCONF = 'wingzen.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wingzen.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(HERE, 'templates').replace('\\', '/')
)

INSTALLED_APPS += (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    #'django.contrib.markup',
    'captcha',
    'chunks',
    'redactor',
    'fluent_comments',
    'crispy_forms',
    'imagekit',
    'django.contrib.comments',
    'django.contrib.flatpages',
    'akismet',
    #'mailer',
    #'markdown',
    'registration',
    'taggit',
    #'testbank',
    'curriculum',
    'guestbook',
    'zenews',
    'wingoa',
    'django_bootstrap_calendar',
    #'debug_toolbar',
    #'guardian',
    #'djangohelper',
    #'BeautifulSoup',
    #'attachments',
    #'onlineuser',
    #'simpleavatar',
    #'pagination',
    #'lbforum',
    #'haystack',
    'microwingzen',
    'DjangoUeditor',
    #'south',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Akismet settings.
AKISMET_API_KEY = 'b7f7b2ab7c8f'
#AKISMET_IS_TEST = True
FLUENT_COMMENTS_CLOSE_AFTER_DAYS = 90
FLUENT_COMMENTS_AKISMET_ACTION = 'moderate'

# Simple-captcha settings.
CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_LETTER_ROTATION = (-16,16)
CAPTCHA_NOISE_FUNCTIONS = None
CAPTCHA_FILTER_FUNCTIONS = ('captcha.helpers.post_smooth',)
CAPTCHA_FONT_SIZE = 20

# redactor(WYSIWYG editor) options.
REDACTOR_OPTIONS = {
    'lang': 'zh_cn',
    'toolbar': 'default',
}
REDACTOR_UPLOAD = 'redactor_upload/'

# registration settings.
ACCOUNT_ACTIVATION_DAYS = 7
LOGIN_REDIRECT_URL = '/'
EMAIL_HOST= 'smtp.gmail.com'
EMAIL_PORT= 25
EMAIL_HOST_USER = 'zouyaoxin@gmail.com'
EMAIL_HOST_PASSWORD = 'iyuelcaynbzfmrwd'
EMAIL_USE_TLS = True

# For custom user model.
#AUTH_USER_MODEL = 'wingoa.staff'

# For debug_toobal settings
#INTERNAL_IPS = ('127.0.0.1',)

# For Authentication backends.
#AUTHENTICATION_BACKENDS = (
#    'django.contrib.auth.backends.ModelBackend',
#    'guardian.backends.ObjectPermissionBackend',
#)
#ANONYMOUS_USER_ID = False

# For DjangoUeditor settings
UEDITOR_TOOLBARS = {
    "wiztopic": [
            ['source','|','cleardoc','undo', 'redo', 'drafts', '|', 'link', 'unlink','|','map', 'music', 'insertvideo','|', 'insertable', 'insertrow', 'insertcol', 'mergeright', 'mergedown', 'deleterow', 'deletecol', 'splittorows', 'splittocols', 'mergecells'],
            [ 'pasteplain','|', 'bold', 'italic', 'underline', 'removeformat', 'formatmatch', 'autotypeset','|', 'forecolor', 'backcolor','|', 'simpleupload', 'insertimage', 'attachment', 'emotion', '|', 'print', 'preview', ]
        ],
    "wizcomment": [
            ['source','|','cleardoc','undo', 'redo', 'drafts', '|', 'link', 'unlink','|','map', '|', 'insertable', 'insertrow', 'insertcol', 'deleterow', 'deletecol', 'splittorows', 'splittocols', ],
            [ 'pasteplain','|', 'bold', 'italic', 'underline', 'removeformat', 'formatmatch', 'autotypeset','|', 'forecolor', 'backcolor','|', 'simpleupload', 'insertimage', 'attachment', 'emotion', ]
        ],
}

UEDITOR_SETTINGS_TOPIC = {
    "toolbars": UEDITOR_TOOLBARS["wiztopic"],
    "initialFrameWidth": 1130,
}

UEDITOR_SETTINGS_COMMENT = {
    "toolbars": UEDITOR_TOOLBARS["wizcomment"],
    "initialFrameWidth": 900,
    "initialFrameHeight": 200,
}

UPLOAD_SETTINGS_TOPIC = {
    "videoMaxSize": 10240000,
    "fileMaxSize": 5120000,
    "imagePathFormat": "ueditor/topic/images/",
    "filePathFormat": "ueditor/topic/files/",
}

UPLOAD_SETTINGS_COMMENT = {
    "videoMaxSize": 5120000,
    "fileMaxSize": 2560000,
    "imagePathFormat": "ueditor/comment/images/",
    "filePathFormat": "ueditor/comment/files/",
}

