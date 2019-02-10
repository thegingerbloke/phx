from .base import *  # noqa

# Set debug mode
DEBUG = False

# Generate a new secret key, e.g.
# https://www.miniwebtool.com/django-secret-key-generator/
SECRET_KEY = '...'

# Update to contain the expected URL of the production site
HOST = 'https://...'

# Update to contain the URL(s) that the site will be hosted on
ALLOWED_HOSTS = [
    '...',
]

# Add production database config
# DATABASES = {
#     'default': {
#     }
# }

# Add production email settings
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_HOST_USER = '...@gmail.com'
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER

# Add error reporting email accounts
ADMINS = []

# Add production email recipient
CONTACT_EMAIL = EMAIL_HOST_USER

# Add production twitter keys
TWITTER = {
    'consumer_key': '...',
    'consumer_secret': '...',
    'oauth_token': '...',
    'oauth_secret': '...',
}

# Add production facebook keys
FACEBOOK = {
    'access_token': '...',
}

# Add production Google Analytics key
ANALYTICS = '...'

# Add IP addresses to enable the debug toolbar
INTERNAL_IPS = []

# SSL
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'

# SECURE_SSL_REDIRECT = True

# https://docs.djangoproject.com/en/2.1/ref/settings/#std:setting-SECURE_PROXY_SSL_HEADER
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
