# Local development Django settings overrides
from .base import *
import os

DEBUG = True

db_host = os.environ.get('POSTGRES_PORT_5432_TCP_ADDR')
db_port = os.environ.get('POSTGRES_PORT_5432_TCP_PORT')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'miracle_metadata',
        'USER': 'miracle',
        'PASSWORD': 'CHANGEME',
        'HOST': db_host,
        'PORT': db_port,
    },
    'datasets': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'miracle_data',
        'USER': 'miracle',
        'PASSWORD': 'CHANGEME',
        'HOST': db_host,
        'PORT': db_port,
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
    )

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# disabling i18n until we need it
USE_I18N = False

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'customize this local secret key'

SOCIAL_AUTH_FACEBOOK_KEY = 'customize this local secret key'
SOCIAL_AUTH_FACEBOOK_SECRET = 'customize this local secret key'

SOCIAL_AUTH_TWITTER_KEY = 'customize this local secret key'
SOCIAL_AUTH_TWITTER_SECRET = 'customize this local secret key'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = 'customize this local secret key'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'customize this local secret key'

SOCIAL_AUTH_GITHUB_KEY = 'customize this local secret key'
SOCIAL_AUTH_GITHUB_SECRET = 'customize this local secret key'

if not os.path.exists(MEDIA_ROOT):
    print("MEDIA_ROOT path '{}' does not exist, trying to create it now.".format(MEDIA_ROOT))
    try:
        os.makedirs(MEDIA_ROOT)
    except:
        print("Unable to create path {}, user uploads will not work properly.".format(MEDIA_ROOT))
