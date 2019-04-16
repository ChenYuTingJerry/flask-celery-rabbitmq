from flask import Flask, jsonify
from flask_restplus import Api, Resource

from api import Task, TaskStatus

app = Flask(__name__)
app.config.from_object('config')

api = Api(app)
api.add_resource(Task, '/task')
api.add_resource(TaskStatus, '/status/<task_id>')

if __name__ == '__main__':
    app.run(debug=True)
