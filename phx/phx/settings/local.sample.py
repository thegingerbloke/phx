from .base import *

# Set debug mode
DEBUG = True

# Generate a new secret key, e.g.
# https://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = 'k@sf6to-5%xri=u0gqyzez2&ypvo+hp&)e4pp$czwn&*ue5*_3'

# Update to contain the expected URL of the local site
HOST = 'http://127.0.0.1:8000'

# Update to contain the URL(s) that the site will be hosted on
ALLOWED_HOSTS = [
  '127.0.0.1',
  'localhost',
]

# Add local database config
# DATABASES = {
#     'default': {
#     }
# }

# Add local email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Add local email recipient
CONTACT_EMAIL = '...@gmail.com'

# Add local twitter keys
TWITTER = {
    'consumer_key': '...',
    'consumer_secret': '...',
    'oauth_token': '...',
    'oauth_secret': '...',
}

# Add local facebook keys
FACEBOOK = {
  'page_id': '...',
  'access_token': '...'
}

# Add local Google Analytics key
ANALYTICS = '...'

# Add IP addresses to enable the debug toolbar
INTERNAL_IPS = [
  '127.0.0.1'
]
