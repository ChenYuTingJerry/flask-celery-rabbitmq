# flask-celery-poc

## Execution

### Windows

```unix
pip install eventlet
celery worker -A celery_worker.celery --loglevel=info --pool=eventlet
```

### Ubuntu or Mac

```unix
celery worker -A celery_worker.celery --loglevel=info
```

### Docker-Compose

```unix
docker-compose up --build
```