import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'BasketballLeague.settings')

app = Celery('BasketballLeague')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
