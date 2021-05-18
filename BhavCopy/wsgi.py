import os

from django.core.wsgi import get_wsgi_application

if eval(os.environ.get('IS_PRODUCTION')):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BhavCopy.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BhavCopy.settings.local')

application = get_wsgi_application()
