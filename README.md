# Flask Celery RabbitMQ

A basic [Docker Compose](https://docs.docker.com/compose/) template for orchestrating a [Flask](http://flask.pocoo.org/) application & a [Celery](http://www.celeryproject.org/) queue with [RabbitMQ](https://www.rabbitmq.com/).

## Installation

```unix
git clone https://github.com/ChenYuTingJerry/flask-celery-rabbitmq.git
```

### Build and Run

```unix
docker-compose up --build
```

To shut down:

 ```unix
docker-compose down
```

To change the endpoints, update the code in api/app.py

Task changes should happen in celery-queue/{module}/tasks.py
