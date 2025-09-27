import unittest
from app.models import User, Task
from app.storage import InMemoryDB  # Adjust import path as needed

class TestInMemoryDB(unittest.TestCase):

    def setUp(self):
        self.db = InMemoryDB()

    def test_create_user(self):
        user = self.db.create_user("alice", "password123")
        self.assertIsInstance(user, User)
        self.assertIn(user.id, self.db.users)
        self.assertEqual(self.db.users[user.id].username, "alice")

    def test_get_user_by_username(self):
        self.db.create_user("bob", "securepass")
        user = self.db.get_user_by_username("bob")
        self.assertIsNotNone(user)
        self.assertEqual(user.username, "bob")

        no_user = self.db.get_user_by_username("charlie")
        self.assertIsNone(no_user)

    def test_create_task(self):
        user = self.db.create_user("dave", "pass")
        task = self.db.create_task("Do laundry", user.id)
        self.assertIsInstance(task, Task)
        self.assertIn(task.id, self.db.tasks)
        self.assertEqual(task.owner_id, user.id)

    def test_list_tasks(self):
        user1 = self.db.create_user("eve", "pass")
        user2 = self.db.create_user("frank", "pass")
        self.db.create_task("Task 1", user1.id)
        self.db.create_task("Task 2", user1.id)
        self.db.create_task("Task 3", user2.id)

        tasks_user1 = self.db.list_tasks(user1.id)
        tasks_user2 = self.db.list_tasks(user2.id)

        self.assertEqual(len(tasks_user1), 2)
        self.assertEqual(len(tasks_user2), 1)

    def test_update_task(self):
        user = self.db.create_user("grace", "pass")
        task = self.db.create_task("Old Title", user.id)

        updated = self.db.update_task(task.id, {"title": "New Title", "done": True})
        self.assertIsNotNone(updated)
        self.assertEqual(updated.title, "New Title")
        self.assertTrue(updated.done)

        nonexistent = self.db.update_task("fake-id", {"title": "X"})
        self.assertIsNone(nonexistent)

    def test_delete_task(self):
        user = self.db.create_user("heidi", "pass")
        task = self.db.create_task("Delete me", user.id)

        result = self.db.delete_task(task.id)
        self.assertTrue(result)
        self.assertNotIn(task.id, self.db.tasks)

        result_false = self.db.delete_task("nonexistent-id")
        self.assertFalse(result_false)

if __name__ == "__main__":
    unittest.main()
