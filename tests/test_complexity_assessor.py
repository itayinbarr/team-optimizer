import unittest
from src.task_management.complexity_assessor import assess_task_complexity, assess_all_tasks

class TestComplexityAssessor(unittest.TestCase):
    def test_assess_task_complexity(self):
        task_description = "Implement a simple feature."
        complexity = assess_task_complexity(task_description)
        self.assertIsInstance(complexity, str)
    
    def test_assess_all_tasks(self):
        task_descriptions = {"task1": "Implement a simple feature."}
        complexities = assess_all_tasks(task_descriptions)
        self.assertIsInstance(complexities, dict)
        self.assertIn("task1", complexities)

if __name__ == "__main__":
    unittest.main()
