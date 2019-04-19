import json

from flask import jsonify, request
from flask_restplus import Resource

from crawler.tasks import parse_web_links
from file.tasks import get_python_package, get_multi_python_packages

tasks = {
    'GetPythonPackage': get_python_package,
    'GetMultiPythonPackage': get_multi_python_packages,
    'ParseWebLinks': parse_web_links
}


class Task(Resource):
    def post(self):
        task, kwargs = parse_task(request.data)
        info = task.apply_async(kwargs=kwargs)
        return jsonify({'info': info.id})


def parse_task(req_data):
    body = json.loads(req_data)
    task = tasks.get(body['task'])
    kwargs = body['meta']
    return task, kwargs


class TaskStatus(Resource):
    def get(self, task_id):
        task = tasks.parse_web_link.AsyncResult(task_id)
        if task.state == 'PENDING':
            response = {
                'state': task.state
            }
        elif task.state != 'FAILURE':
            response = {
                'state': task.state,
                'result': task.get()
            }
        else:
            # something went wrong in the background job
            response = {
                'state': task.state,
            }
        return jsonify(response)
