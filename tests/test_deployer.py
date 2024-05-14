import unittest
import os
import json
from src.pipeline.deployer import deploy_tasks

class TestDeployer(unittest.TestCase):
    def setUp(self):
        self.tasks_directory = "tests/reviewed_tasks"
        self.deployment_directory = "tests/deployed_tasks"
        os.makedirs(self.tasks_directory, exist_ok=True)
        os.makedirs(self.deployment_directory, exist_ok=True)
        task = {"description": "Deploy this task"}
        with open(os.path.join(self.tasks_directory, "reviewed_task1.json"), 'w') as f:
            json.dump(task, f)

    def test_deploy_tasks(self):
        deploy_tasks(self.tasks_directory, self.deployment_directory)
        self.assertTrue(os.path.exists(os.path.join(self.deployment_directory, "reviewed_task1.json")))

    def tearDown(self):
        for directory in [self.tasks_directory, self.deployment_directory]:
            for file in os.listdir(directory):
                file_path = os.path.join(directory, file)
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            os.rmdir(directory)

if __name__ == "__main__":
    unittest.main()
