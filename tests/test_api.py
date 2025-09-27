
import json
from app.api import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

def setup_user(client):
    client.post("/register", json={"username": "bob", "password": "pw"})

def test_task_crud():
    app = create_app()
    client = app.test_client()
    setup_user(client)

    # Create task
    r = client.post("/tasks", json={"username": "bob", "title": "write tests"})
    assert r.status_code == 201
    task = r.get_json()
    tid = task["id"]

    # List tasks
    r = client.get("/tasks/bob")
    assert r.status_code == 200
    assert len(r.get_json()) == 1

    # Update task
    r = client.put(f"/tasks/{tid}", json={"done": True})
    assert r.status_code == 200
    assert r.get_json()["done"] is True

    # Delete task
    r = client.delete(f"/tasks/{tid}")
    assert r.status_code == 200

    # Verify deletion
    r = client.get("/tasks/bob")
    assert r.status_code == 200
    assert len(r.get_json()) == 0
