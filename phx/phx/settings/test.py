import os

from .base import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'test.sqlite3'),  # noqa
    }
}

HOST = 'http://example.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
