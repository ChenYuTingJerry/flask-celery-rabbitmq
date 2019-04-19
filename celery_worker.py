from celery import Celery
import config

app = Celery(
    'tasks',
    backend=config.CELERY_RESULT_BACKEND,
    broker=config.CELERY_BROKER_URL
)

from crawler import tasks
from file import tasks