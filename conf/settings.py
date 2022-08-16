################################################################################
################################################################################

# Please do not modify this file, it will be reset at the next update.
# You can edit the file __FINALPATH__/local_settings.py and add/modify the settings you need.
# The parameters you add in local_settings.py will overwrite these,
# but you can use the options and documentation in this file to find out what can be done.

################################################################################
################################################################################

from pathlib import Path as __Path

from django.core.validators import EmailValidator as __EmailValidator
from django_yunohost_integration.base_settings import *  # noqa
from django_yunohost_integration.secret_key import get_or_create_secret as __get_or_create_secret

from djfritz_project.settings.base import *  # noqa


FINALPATH = __Path('__FINALPATH__')  # /opt/yunohost/$app
assert FINALPATH.is_dir(), f'Directory not exists: {FINALPATH}'

PUBLIC_PATH = __Path('__PUBLIC_PATH__')  # /var/www/$app
assert PUBLIC_PATH.is_dir(), f'Directory not exists: {PUBLIC_PATH}'

LOG_FILE = __Path('__LOG_FILE__')  # /var/log/$app/django_example_ynh.log
assert LOG_FILE.is_file(), f'File not exists: {LOG_FILE}'

PATH_URL = '__PATH_URL__'  # $YNH_APP_ARG_PATH
PATH_URL = PATH_URL.strip('/')

# -----------------------------------------------------------------------------
# config_panel.toml settings:


DEBUG_ENABLED = '__DEBUG_ENABLED__'
LOG_LEVEL = '__LOG_LEVEL__'
ADMIN_EMAIL = '__ADMIN_EMAIL__'
DEFAULT_FROM_EMAIL = '__DEFAULT_FROM_EMAIL__'

# -----------------------------------------------------------------------------
# Use/convert/validate config_panel.toml settings:

DEBUG = bool(int(DEBUG_ENABLED))
assert LOG_LEVEL in (
    'DEBUG',
    'INFO',
    'WARNING',
    'ERROR',
    'CRITICAL',
), f'Invalid LOG_LEVEL: {LOG_LEVEL!r}'
__EmailValidator(
    message='ADMIN_EMAIL %(value)r from config panel is not valid!',
)(ADMIN_EMAIL)
__EmailValidator(
    message='DEFAULT_FROM_EMAIL %(value)r from config panel is not valid!',
)(DEFAULT_FROM_EMAIL)

# -----------------------------------------------------------------------------

# Function that will be called to finalize a user profile:
YNH_SETUP_USER = 'setup_user.setup_project_user'

SECRET_KEY = __get_or_create_secret(FINALPATH / 'secret.txt')  # /opt/yunohost/$app/secret.txt

INSTALLED_APPS += [
    'axes',  # https://github.com/jazzband/django-axes
    'django_yunohost_integration',  # https://github.com/YunoHost-Apps/django_yunohost_integration
]

MIDDLEWARE.insert(
    MIDDLEWARE.index('django.contrib.auth.middleware.AuthenticationMiddleware') + 1,
    # login a user via HTTP_REMOTE_USER header from SSOwat:
    'django_yunohost_integration.sso_auth.auth_middleware.SSOwatRemoteUserMiddleware',
)
# AxesMiddleware should be the last middleware:
MIDDLEWARE.append('axes.middleware.AxesMiddleware')


# Keep ModelBackend around for per-user permissions and superuser
AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesBackend',  # AxesBackend should be the first backend!
    #
    # Authenticate via SSO and nginx 'HTTP_REMOTE_USER' header:
    'django_yunohost_integration.sso_auth.auth_backend.SSOwatUserBackend',
    #
    # Fallback to normal Django model backend:
    'django.contrib.auth.backends.ModelBackend',
)

LOGIN_REDIRECT_URL = None
LOGIN_URL = '/yunohost/sso/'
LOGOUT_REDIRECT_URL = '/yunohost/sso/'


# -----------------------------------------------------------------------------

ROOT_URLCONF = 'urls'  # ./conf/urls.py

ADMINS = (('__ADMIN__', ADMIN_EMAIL),)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '__DB_NAME__',
        'USER': '__DB_USER__',
        'PASSWORD': '__DB_PWD__',
        'HOST': '127.0.0.1',
        'PORT': '5432',  # Default Postgres Port
        'CONN_MAX_AGE': 600,
    }
}

# Title of site to use
SITE_TITLE = '__APP__'

# Site domain
SITE_DOMAIN = '__DOMAIN__'

# Subject of emails includes site title
EMAIL_SUBJECT_PREFIX = f'[{SITE_TITLE}] '


# E-mail address that error messages come from.
SERVER_EMAIL = 'noreply@__DOMAIN__'

# Default email address to use for various automated correspondence from
# the site managers. Used for registration emails.

# List of URLs your site is supposed to serve
ALLOWED_HOSTS = ['__DOMAIN__']

# _____________________________________________________________________________
# Configuration for caching
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/__REDIS_DB__',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
        'KEY_PREFIX': '__APP__',
    },
}

# _____________________________________________________________________________
# Static files (CSS, JavaScript, Images)

if PATH_URL:
    STATIC_URL = f'/{PATH_URL}/static/'
    MEDIA_URL = f'/{PATH_URL}/media/'
else:
    # Installed to domain root, without a path prefix?
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'

STATIC_ROOT = str(PUBLIC_PATH / 'static')
MEDIA_ROOT = str(PUBLIC_PATH / 'media')


# -----------------------------------------------------------------------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '{asctime} {levelname} {name} {module}.{funcName} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'formatter': 'verbose',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'log_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'formatter': 'verbose',
            'filename': str(LOG_FILE),
        },
    },
    'loggers': {
        '': {'handlers': ['log_file', 'mail_admins'], 'level': LOG_LEVEL, 'propagate': False},
        'django': {'handlers': ['log_file', 'mail_admins'], 'level': LOG_LEVEL, 'propagate': False},
        'axes': {'handlers': ['log_file', 'mail_admins'], 'level': LOG_LEVEL, 'propagate': False},
        'django_tools': {
            'handlers': ['log_file', 'mail_admins'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'django_yunohost_integration': {
            'handlers': ['log_file', 'mail_admins'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
        'djfritz': {
            'handlers': ['log_file', 'mail_admins'],
            'level': LOG_LEVEL,
            'propagate': False,
        },
    },
}

# -----------------------------------------------------------------------------

try:
    from local_settings import *  # noqa
except ImportError:
    pass
