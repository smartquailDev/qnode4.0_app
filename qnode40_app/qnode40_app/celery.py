import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'qnode40_app.settings')

app = Celery('qnode40_app')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
