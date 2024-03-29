from config.settings.base import *

DEBUG = False

ALLOWED_HOSTS = ['your-production-domain.com']

# Configure production database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'prod_db',
        'USER': 'postgres',
        "PASSWORD": "0576",
        "HOST": "localhost",
        "PORT": 5432,
    }
}