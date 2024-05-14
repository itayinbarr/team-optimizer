import unittest
import os
import json
from src.task_management.review import review_tasks, save_reviewed_tasks

class TestReview(unittest.TestCase):
    def setUp(self):
        self.tasks = {"task1": {"description": "Simple task"}}
        self.complexities = {"task1": "Simple"}
        self.directory = "tests/reviewed_tasks"
        os.makedirs(self.directory, exist_ok=True)

    def test_review_tasks(self):
        reviewed_tasks = review_tasks(self.tasks, self.complexities)
        self.assertIsInstance(reviewed_tasks, dict)
        self.assertIn("task1", reviewed_tasks)
        self.assertEqual(reviewed_tasks["task1"], self.tasks["task1"])

    def test_save_reviewed_tasks(self):
        reviewed_tasks = {"task1": self.tasks["task1"]}
        save_reviewed_tasks(reviewed_tasks, self.directory)
        self.assertTrue(os.path.exists(os.path.join(self.directory, "reviewed_task1.json")))

    def tearDown(self):
        for file in os.listdir(self.directory):
            file_path = os.path.join(self.directory, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        os.rmdir(self.directory)

if __name__ == "__main__":
    unittest.main()
