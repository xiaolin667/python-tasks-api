
from dataclasses import dataclass, asdict
from typing import Dict
import uuid

@dataclass
class Task:
    id: str
    title: str
    done: bool = False

    def to_dict(self) -> Dict:
        """Convert Task object to dictionary for JSON serialization."""
        return asdict(self)

    @staticmethod
    def new(title: str, done: bool = False) -> "Task":
        """Factory method to create a new Task with a unique ID."""
        return Task(id=str(uuid.uuid4()), title=title, done=done)
