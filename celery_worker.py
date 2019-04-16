from celery import Celery
import config

celery = Celery(
    'tasks',
    backend=config.CELERY_RESULT_BACKEND,
    broker=config.CELERY_BROKER_URL
)

from moduleA import tasks