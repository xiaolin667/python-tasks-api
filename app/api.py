
from flask import Flask, jsonify, request
from app.storage import TaskStorage
from app.version import __version__

def create_app():
    app = Flask(__name__)
    store = TaskStorage()

    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(status="ok", version=__version__)

    @app.route("/tasks", methods=["GET"])
    def list_tasks():
        return jsonify(store.list())

    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.get_json() or {}
        task = store.create(data.get("title", ""), data.get("done", False))
        return jsonify(task), 201

    @app.route("/tasks/<task_id>", methods=["GET"])
    def get_task(task_id):
        task = store.get(task_id)
        return (jsonify(task), 200) if task else (jsonify(error="not found"), 404)

    @app.route("/tasks/<task_id>", methods=["PUT"])
    def update_task(task_id):
        data = request.get_json() or {}
        task = store.update(task_id, data)
        return (jsonify(task), 200) if task else (jsonify(error="not found"), 404)

    @app.route("/tasks/<task_id>", methods=["DELETE"])
    def delete_task(task_id):
        ok = store.delete(task_id)
        return (jsonify(status="deleted"), 200) if ok else (jsonify(error="not found"), 404)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
