from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'skyscrapper.settings')

app = Celery('skyscrapper')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


####### README: is possible to set periodic tasks at the beginning, however, best done from the admin panel
#@app.on_configure.connect
#def setup_periodic_tasks(sender, **kwargs):
    # work
#    sender.add_periodic_task(10.0, test.s(2,3), expires=10, name='add every 10')
