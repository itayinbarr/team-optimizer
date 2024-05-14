import unittest
from src.meeting_minutes.processor import extract_action_items, process_all_minutes

class TestProcessor(unittest.TestCase):
    def test_extract_action_items(self):
        minutes = "Action Item: Do something\nAction Item: Do another thing"
        action_items = extract_action_items(minutes)
        self.assertEqual(len(action_items), 2)
        self.assertIn("Do something", action_items)
    
    def test_process_all_minutes(self):
        minutes_dict = {"meeting1.txt": "Action Item: Do something\nAction Item: Do another thing"}
        all_action_items = process_all_minutes(minutes_dict)
        self.assertIsInstance(all_action_items, dict)
        self.assertIn("meeting1.txt", all_action_items)
        self.assertEqual(len(all_action_items["meeting1.txt"]), 2)

if __name__ == "__main__":
    unittest.main()
