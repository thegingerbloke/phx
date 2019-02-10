"""
Base env-parsing settings

Applied to all envs

See https://django-environ.readthedocs.io/
"""

import os

import environ

from .app import *  # noqa

# app roots
django_root = environ.Path(__file__) - 3
app_root = environ.Path(django_root) - 1

# init env
env = environ.Env()

# reading .env file
environ.Env.read_env(os.path.join(app_root(), '.env'))

SITE_ROOT = django_root()

# False if not in os.environ
DEBUG = env.bool('DEBUG')
TEMPLATE_DEBUG = DEBUG

# Raise ImproperlyConfigured exception if DATABASE_URL not in os.environ
DATABASES = {
    'default': env.db(),
    # 'default': env.db('SQLITE_URL', default='sqlite:///tmp-sqlite.db')
}

MEDIA_ROOT = app_root('media')
MEDIA_URL = '/media/'

STATIC_ROOT = app_root('static')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    os.path.join(app_root(), 'frontend', 'static'),
]

# Raise ImproperlyConfigured exception if SECRET_KEY not in os.environ
SECRET_KEY = env.str('SECRET_KEY')

# Hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', [])

# Site URL
HOST = env.str('HOST', 'http://localhost:8000/')

# App-specific settings
CONTACT_EMAIL = env.list('CONTACT_EMAIL')
ADMINS = env.list('ADMINS', default=[])

# Analytics
if env.str('ANALYTICS', default=''):
    ANALYTICS = env.str('ANALYTICS')

# Twitter
if env.str(
        'TWITTER_CONSUMER_KEY', default='') and env.str(
            'TWITTER_SECRET_KEY', default='') and env.str(
                'TWITTER_OAUTH_TOKEN_KEY', default='') and env.str(
                    'TWITTER_OAUTH_SECRET_KEY', default=''):
    TWITTER = {
        'consumer_key': env.str('TWITTER_CONSUMER_KEY'),
        'consumer_secret': env.str('TWITTER_SECRET_KEY'),
        'oauth_token': env.str('TWITTER_OAUTH_TOKEN_KEY'),
        'oauth_secret': env.str('TWITTER_OAUTH_SECRET_KEY'),
    }

# Facebook
if env.str(
        'FACEBOOK_PAGE_ID_KEY', default='') and env.str(
            'FACEBOOK_ACCESS_TOKEN_KEY', default=''):
    FACEBOOK = {
        'page_id': env.str('FACEBOOK_PAGE_ID_KEY'),
        'access_token': env.str('FACEBOOK_ACCESS_TOKEN_KEY')
    }
