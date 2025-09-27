import unittest
from uuid import UUID
from app.models import User, Task

class TestUserTaskModels(unittest.TestCase):

    def test_user_creation(self):
        username = "testuser"
        password = "securepassword"
        user = User.new(username, password)

        # Check types and values
        self.assertIsInstance(user, User)
        self.assertEqual(user.username, username)
        self.assertEqual(user.password, password)
        self.assertTrue(UUID(user.id))  # Valid UUID

    def test_user_to_dict(self):
        user = User.new("alice", "password123")
        user_dict = user.to_dict()

        self.assertEqual(set(user_dict.keys()), {"id", "username"})
        self.assertEqual(user_dict["id"], user.id)
        self.assertEqual(user_dict["username"], user.username)

    def test_task_creation_defaults(self):
        user = User.new("bob", "pass")
        task = Task.new("Buy milk", owner_id=user.id)

        self.assertIsInstance(task, Task)
        self.assertEqual(task.title, "Buy milk")
        self.assertFalse(task.done)
        self.assertEqual(task.owner_id, user.id)
        self.assertTrue(UUID(task.id))  # Valid UUID

    def test_task_creation_custom_done(self):
        user = User.new("carol", "pass")
        task = Task.new("Submit report", owner_id=user.id, done=True)

        self.assertTrue(task.done)

    def test_task_to_dict(self):
        user = User.new("dave", "pass")
        task = Task.new("Walk dog", owner_id=user.id)
        task_dict = task.to_dict()

        self.assertEqual(task_dict["id"], task.id)
        self.assertEqual(task_dict["title"], task.title)
        self.assertEqual(task_dict["done"], task.done)
        self.assertEqual(task_dict["owner_id"], task.owner_id)

if __name__ == "__main__":
    unittest.main()
