from __future__ import absolute_import
import json
from celery import states
from flask import Flask, jsonify, request
from flask_restplus import Api, Resource

from woker import celery

app = Flask(__name__)

api = Api(app)

tasks = {
    'GetPythonPackage': "file.tasks.get_python_package",
    'GetMultiPythonPackage': "file.tasks.get_multi_python_packages",
    'ParseWebLinks': "crawler.tasks.parse_web_links"
}


class Task(Resource):
    def post(self):
        task, kwargs = parse_task(request.data)
        info = celery.send_task(task, kwargs=kwargs)
        return jsonify({'info': info.id})


def parse_task(req_data):
    body = json.loads(req_data)
    task = tasks.get(body['task'])
    kwargs = body['meta']
    return task, kwargs


class TaskStatus(Resource):
    def get(self, task_id):
        res = celery.AsyncResult(task_id)
        if res.state == states.PENDING:
            return res.state
        else:
            return str(res.result)


api.add_resource(Task, '/task')
api.add_resource(TaskStatus, '/status/<string:task_id>')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
