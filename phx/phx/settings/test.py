import os

from .base import *  # noqa

HOST = 'http://example.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db_test.sqlite3'),  # noqa
    }
}
