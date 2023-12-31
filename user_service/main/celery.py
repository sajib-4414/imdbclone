# django_db_task/celery.py

import os
from celery import Celery
from django.conf import settings

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE', 
    'main.settings'
)

app = Celery('main')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# Auto-discover tasks in all installed apps.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)