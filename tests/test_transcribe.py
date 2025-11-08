import unittest
from backend.src.transcribe import transcribe_audio

class TestTranscribe(unittest.TestCase):
    
    def test_transcribe_audio_valid(self):
        # Test with a valid audio file
        audio_file = 'example_audio/sample_call.wav'
        result = transcribe_audio(audio_file)
        self.assertIsInstance(result, dict)
        self.assertIn('transcript', result)
        self.assertIn('timestamps', result)

    def test_transcribe_audio_invalid(self):
        # Test with an invalid audio file
        audio_file = 'example_audio/invalid_file.wav'
        with self.assertRaises(FileNotFoundError):
            transcribe_audio(audio_file)

    def test_transcribe_audio_empty(self):
        # Test with an empty audio file
        audio_file = 'example_audio/empty.wav'
        result = transcribe_audio(audio_file)
        self.assertEqual(result['transcript'], "")
        self.assertEqual(result['timestamps'], [])

if __name__ == '__main__':
    unittest.main()