"""
WSGI config for dj_rest_multiple_file_upload_sample project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_rest_multiple_file_upload_sample.settings')

application = get_wsgi_application()
