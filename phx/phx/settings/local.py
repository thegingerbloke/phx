from .base import *  # noqa

INSTALLED_APPS += [  # noqa
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE  # noqa

# Add local email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Add IP addresses to enable the debug toolbar
INTERNAL_IPS = ['127.0.0.1']
