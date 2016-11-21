import os, sys

sys.path.append('c:\apache24\htdocs\mortythemage')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mortythemage.settings'
PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()