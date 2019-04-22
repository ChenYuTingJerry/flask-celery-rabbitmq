from celery import Celery

CELERY_RESULT_BACKEND = 'amqp://admin:mypass@rabbit'
CELERY_BROKER_URL = 'amqp://admin:mypass@rabbit'

app = Celery(
    'tasks',
    backend=CELERY_RESULT_BACKEND,
    broker=CELERY_BROKER_URL
)

# app.autodiscover_tasks('celery-queue')
from crawler import tasks
from file import tasks
