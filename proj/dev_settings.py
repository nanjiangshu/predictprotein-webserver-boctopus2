"""
Django settings for proj project in development.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
try:
    from shared_settings import *
except ImportError:
    pass

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5&!cq9#+(_=!ou=mco0=-qrmn6h66o(f)h$ho4+0vo1#d24xdy'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', 'boctopus.topcons.net', 'b2.topcons.net', 'www.b2.topcons.net', 'boctopus.cbr.su.se', 'boctopus.bioinfo.se', 'dev.boctopus.bioinfo.se']

STATIC_ROOT = "/var/www/html/boctopus2/proj/pred/static"

