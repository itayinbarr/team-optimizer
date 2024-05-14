import unittest
from src.meeting_minutes.transcriber import transcribe_audio, transcribe_all_audios
import os

class TestTranscriber(unittest.TestCase):
    def test_transcribe_audio(self):
        # Assuming a sample.wav file exists in the tests directory
        audio_path = "tests/sample.wav"
        transcript = transcribe_audio(audio_path)
        self.assertIsInstance(transcript, str)
    
    def test_transcribe_all_audios(self):
        directory = "tests/audios"
        os.makedirs(directory, exist_ok=True)
        # Create a dummy audio file for testing
        with open(os.path.join(directory, "sample.wav"), "w") as f:
            f.write("dummy data")
        transcripts = transcribe_all_audios(directory)
        self.assertIsInstance(transcripts, dict)
        self.assertIn("sample.wav", transcripts)

if __name__ == "__main__":
    unittest.main()
