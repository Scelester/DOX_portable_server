"""
WSGI config for tempoTest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
import os,sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application


path_hone = str(Path(__file__).parents[1])

if path_hone not in sys.path:
    sys.path.append(path_hone)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tempoTest.settings')

application = get_wsgi_application()