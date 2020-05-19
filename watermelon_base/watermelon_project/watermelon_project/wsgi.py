"""
WSGI config for watermelon_project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys
 
sys.path.append('/home/ubuntu/watermelon_base/watermelon_project')
sys.path.append('/home/ubuntu/watermelon_base/watermelon_venv/lib/python3.5/site-packages')
 
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watermelon_project.settings")
 
application = get_wsgi_application()
