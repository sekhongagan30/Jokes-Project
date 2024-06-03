import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jokes_project.settings')

app = Celery('jokes_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'get_joke_3s': {
        'task': 'jokes.tasks.get_joke', # task is fn get_joke in file tasks of jokes app
        'schedule': 3.0 # schedule is : after how many seconds it shud call the task
    }
}

app.autodiscover_tasks()
