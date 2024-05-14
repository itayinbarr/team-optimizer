import unittest
import os
import json
from src.task_management.task_handler import load_tasks, save_task

class TestTaskHandler(unittest.TestCase):
    def setUp(self):
        self.directory = "tests/tasks"
        os.makedirs(self.directory, exist_ok=True)
        self.task = {"description": "Implement feature A"}

    def test_load_tasks(self):
        with open(os.path.join(self.directory, "task1.json"), 'w') as f:
            json.dump(self.task, f)
        tasks = load_tasks(self.directory)
        self.assertIsInstance(tasks, dict)
        self.assertIn("task1.json", tasks)

    def test_save_task(self):
        save_task(self.task, "task2.json", self.directory)
        self.assertTrue(os.path.exists(os.path.join(self.directory, "task2.json")))

    def tearDown(self):
        for file in os.listdir(self.directory):
            file_path = os.path.join(self.directory, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
        os.rmdir(self.directory)

if __name__ == "__main__":
    unittest.main()
