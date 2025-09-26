
from app.storage import TaskStorage

def test_create_list_get_update_delete():
    s = TaskStorage()
    t = s.create("demo", False)
    assert t["title"] == "demo"
    assert len(s.list()) == 1
    got = s.get(t["id"])
    assert got["id"] == t["id"]
    updated = s.update(t["id"], {"done": True})
    assert updated["done"] is True
    assert s.delete(t["id"]) is True
    assert s.get(t["id"]) is None
