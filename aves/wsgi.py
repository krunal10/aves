import os
from os.path import abspath, dirname
from sys import path

from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "api.settings")

application = DjangoWhiteNoise(get_wsgi_application())
