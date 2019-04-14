import random
import time

from flask import jsonify, url_for, request

from app import create_app

app = create_app()

# Initialize Celery
from app.celery import make_celery

celery = make_celery(app)


@app.route('/entry', methods=['POST'])
def api_entry():
    task_name = request.args.get('task')

    return jsonify({}), 202


if __name__ == '__main__':
    app.run(debug=True)
