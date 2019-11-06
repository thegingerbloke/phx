# Test env - used for local test runner

from .app import *  # noqa
from .env import *  # noqa

# Config settings below are manually set here rather than via .env file as
# these tests are generally run while the default .env is active

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, 'test.sqlite3'),  # noqa
    }
}

SITE_URL = 'http://example.com'
