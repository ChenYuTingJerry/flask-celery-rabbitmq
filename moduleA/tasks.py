from celery_worker import celery


@celery.task()
def hello():
    return {'hello': 'world'}
