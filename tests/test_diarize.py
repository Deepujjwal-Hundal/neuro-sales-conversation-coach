import pytest
from backend.src.diarize import diarize_audio

def test_diarize_audio():
    # Test case for a sample audio file
    audio_file = 'example_audio/sample_call.wav'
    expected_output = {
        'speaker_A': [
            {'start': 0.0, 'end': 5.0, 'text': 'Hello, how can I help you?'},
            {'start': 10.0, 'end': 15.0, 'text': 'I see you are interested in our product.'}
        ],
        'speaker_B': [
            {'start': 5.0, 'end': 10.0, 'text': 'I would like to know more about it.'},
            {'start': 15.0, 'end': 20.0, 'text': 'That sounds great!'}
        ]
    }

    output = diarize_audio(audio_file)
    
    assert output == expected_output, "Diarization output does not match expected output."