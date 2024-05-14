import unittest
from src.meeting_minutes.generator import generate_minutes, generate_all_minutes

class TestGenerator(unittest.TestCase):
    def test_generate_minutes(self):
        transcript = "This is a test transcript."
        minutes = generate_minutes(transcript)
        self.assertIsInstance(minutes, str)
    
    def test_generate_all_minutes(self):
        transcripts = {"test.txt": "This is a test transcript."}
        all_minutes = generate_all_minutes(transcripts)
        self.assertIsInstance(all_minutes, dict)
        self.assertIn("test.txt", all_minutes)

if __name__ == "__main__":
    unittest.main()
