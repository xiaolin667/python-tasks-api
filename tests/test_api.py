
import json
from app.api import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json()["status"] == "ok"

def test_crud():
    app = create_app()
    client = app.test_client()
    # Create
    r = client.post("/tasks", json={"title": "write tests"})
    assert r.status_code == 201
    tid = r.get_json()["id"]
    # Read
    r = client.get(f"/tasks/{tid}")
    assert r.status_code == 200
    # Update
    r = client.put(f"/tasks/{tid}", json={"done": True})
    assert r.get_json()["done"] is True
    # Delete
    r = client.delete(f"/tasks/{tid}")
    assert r.status_code == 200
    # Not found
    r = client.get(f"/tasks/{tid}")
    assert r.status_code == 404
