
from typing import Dict, Optional
from app.models import User, Task

class InMemoryDB:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.tasks: Dict[str, Task] = {}

    # User operations
    def create_user(self, username: str, password: str) -> User:
        user = User.new(username, password)
        self.users[user.id] = user
        return user

    def get_user_by_username(self, username: str) -> Optional[User]:
        return next((u for u in self.users.values() if u.username == username), None)

    # Task operations
    def create_task(self, title: str, owner_id: str) -> Task:
        task = Task.new(title, owner_id)
        self.tasks[task.id] = task
        return task

    def list_tasks(self, owner_id: str):
        return [t for t in self.tasks.values() if t.owner_id == owner_id]

    def update_task(self, task_id: str, data: dict) -> Optional[Task]:
        task = self.tasks.get(task_id)
        if not task:
            return None
        task.title = data.get("title", task.title)
        task.done = data.get("done", task.done)
        return task

    def delete_task(self, task_id: str) -> bool:
        return self.tasks.pop(task_id, None) is not None
