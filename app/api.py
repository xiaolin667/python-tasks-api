from flask import Flask, jsonify, request
from app.storage import InMemoryDB
from app.version import __version__
import logging

import sys

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)

db = InMemoryDB()

def home():
    return 'Hello, World!'

def health():
    return jsonify(status="ok", version=__version__)

def register():
    data = request.get_json() or {}
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify(error="username and password required"), 400
    if db.get_user_by_username(username):
        return jsonify(error="user exists"), 400

    user = db.create_user(username, password)
    return jsonify(user.to_dict()), 201

def login():
    data = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password")

    user = db.get_user_by_username(username)
    if not user or user.password != password:
        return jsonify(error="invalid credentials"), 401

    return jsonify(message="login successful", user=user.to_dict())

def create_task():
    data = request.get_json() or {}
    username = data.get("username", "")
    title = data.get("title", "")

    owner = db.get_user_by_username(username)
    if not owner:
        return jsonify(error="invalid user"), 400

    task = db.create_task(title, owner.id)
    return jsonify(task.to_dict()), 201

def list_tasks(username):
    user = db.get_user_by_username(username)
    if not user:
        return jsonify(error="invalid user"), 400

    tasks = [t.to_dict() for t in db.list_tasks(user.id)]
    return jsonify(tasks)

def update_task(task_id):
    data = request.get_json() or {}
    task = db.update_task(task_id, data)

    if not task:
        return jsonify(error="not found"), 404
    return jsonify(task.to_dict()), 200

def delete_task(task_id):
    if db.delete_task(task_id):
        return jsonify(status="deleted"), 200
    return jsonify(error="not found"), 404


def create_app():
    app = Flask(__name__)
    app.logger.handlers = logger.handlers
    app.logger.setLevel(logging.INFO)

    app.add_url_rule('/', 'home', home)
    app.add_url_rule('/health', 'health', health, methods=['GET'])
    app.add_url_rule('/register', 'register', register, methods=['POST'])
    app.add_url_rule('/login', 'login', login, methods=['POST'])
    app.add_url_rule('/tasks', 'create_task', create_task, methods=['POST'])
    app.add_url_rule('/tasks/<username>', 'list_tasks', list_tasks, methods=['GET'])
    app.add_url_rule('/tasks/<task_id>', 'update_task', update_task, methods=['PUT'])
    app.add_url_rule('/tasks/<task_id>', 'delete_task', delete_task, methods=['DELETE'])

    @app.before_request
    def log_request_info():
        logger.info(f"Request: {request.method} {request.path}")
        sys.stdout.flush()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host="0.0.0.0", port=5000)

