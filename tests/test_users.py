
from app.api import create_app

def test_register_and_login():
    app = create_app()
    client = app.test_client()

    # Register
    r = client.post("/register", json={"username": "alice", "password": "secret"})
    assert r.status_code == 201
    user = r.get_json()
    assert user["username"] == "alice"

    # Duplicate register
    r = client.post("/register", json={"username": "alice", "password": "secret"})
    assert r.status_code == 400

    # Login success
    r = client.post("/login", json={"username": "alice", "password": "secret"})
    assert r.status_code == 200
    assert r.get_json()["message"] == "login successful"

    # Login fail
    r = client.post("/login", json={"username": "alice", "password": "wrong"})
    assert r.status_code == 401
