
import uuid

class TaskStorage:
    def __init__(self):
        self._db = {}

    def list(self):
        return list(self._db.values())

    def create(self, title, done=False):
        tid = str(uuid.uuid4())
        task = {"id": tid, "title": title, "done": bool(done)}
        self._db[tid] = task
        return task

    def get(self, tid):
        return self._db.get(tid)

    def update(self, tid, data):
        task = self._db.get(tid)
        if not task:
            return None
        task["title"] = data.get("title", task["title"])
        task["done"] = bool(data.get("done", task["done"]))
        self._db[tid] = task
        return task

    def delete(self, tid):
        return self._db.pop(tid, None) is not None
