from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'phx_test',
        'USER': '',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
    }
}

HOST = 'http://example.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
