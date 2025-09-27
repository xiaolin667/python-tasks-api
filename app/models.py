
from dataclasses import dataclass, asdict
import uuid
from typing import Dict

@dataclass
class User:
    id: str
    username: str
    password: str  # in real apps, hash this!

    def to_dict(self) -> Dict:
        return {"id": self.id, "username": self.username}

    @staticmethod
    def new(username: str, password: str) -> "User":
        return User(id=str(uuid.uuid4()), username=username, password=password)


@dataclass
class Task:
    id: str
    title: str
    done: bool
    owner_id: str

    def to_dict(self) -> Dict:
        return asdict(self)

    @staticmethod
    def new(title: str, owner_id: str, done: bool = False) -> "Task":
        return Task(id=str(uuid.uuid4()), title=title, done=done, owner_id=owner_id)
