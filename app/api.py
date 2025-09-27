Try AI directly in your favourite apps … Use Gemini to generate drafts and refine content, plus get Gemini Pro with access to Google's next-gen AI for $32.99 $0 for 1 month
from flask import Flask, jsonify, request
from app.storage import InMemoryDB
from app.version import __version__

db = InMemoryDB()

def create_app():
    app = Flask(__name__)

    # Health
    @app.route("/health", methods=["GET"])
    def health():
        return jsonify(status="ok", version=__version__)

    # User registration
    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json() or {}
        if not data.get("username") or not data.get("password"):
            return jsonify(error="username and password required"), 400
        if db.get_user_by_username(data["username"]):
            return jsonify(error="user exists"), 400
        user = db.create_user(data["username"], data["password"])
        return jsonify(user.to_dict()), 201

    # Login (very simple, no JWT for demo)
    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json() or {}
        user = db.get_user_by_username(data.get("username", ""))
        if not user or user.password != data.get("password"):
            return jsonify(error="invalid credentials"), 401
        return jsonify(message="login successful", user=user.to_dict())

    # CRUD tasks
    @app.route("/tasks", methods=["POST"])
    def create_task():
        data = request.get_json() or {}
        owner = db.get_user_by_username(data.get("username", ""))
        if not owner:
            return jsonify(error="invalid user"), 400
        task = db.create_task(data.get("title", ""), owner.id)
        return jsonify(task.to_dict()), 201

    @app.route("/tasks/<username>", methods=["GET"])
    def list_tasks(username):
        user = db.get_user_by_username(username)
        if not user:
            return jsonify(error="invalid user"), 400
        return jsonify([t.to_dict() for t in db.list_tasks(user.id)])

    @app.route("/tasks/<task_id>", methods=["PUT"])
    def update_task(task_id):
        data = request.get_json() or {}
        task = db.update_task(task_id, data)
        return (jsonify(task.to_dict()), 200) if task else (jsonify(error="not found"), 404)

    @app.route("/tasks/<task_id>", methods=["DELETE"])
    def delete_task(task_id):
        ok = db.delete_task(task_id)
        return (jsonify(status="deleted"), 200) if ok else (jsonify(error="not found"), 404)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
