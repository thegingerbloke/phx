from .base import *

# Set debug mode
DEBUG = False

# Generate a new secret key, e.g.
# https://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '...'

# Update to contain the expected URL of the dev site
HOST = 'https://...'

# Update to contain the URL(s) that the site will be hosted on
ALLOWED_HOSTS = [
  '...',
]

# Add dev database config
DATABASES = {
    'default': {
    }
}

# Add dev email settings
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = '...@gmail.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Add dev email recipient
CONTACT_EMAIL = '...@gmail.com'

# Add dev twitter keys
TWITTER = {
    'consumer_key': '...',
    'consumer_secret': '...',
    'oauth_token': '...',
    'oauth_secret': '...',
}

# Add dev facebook keys
FACEBOOK = {
  'access_token': '...',
  'page_id': '...',
}

# Add dev Google Analytics key
ANALYTICS = '...'

# Add IP addresses to enable the debug toolbar
INTERNAL_IPS = []
