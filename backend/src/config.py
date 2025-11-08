# File: /neuro-sales-conversation-coach/neuro-sales-conversation-coach/backend/src/config.py

import os

class Config:
    # API keys and other sensitive information
    WHISPER_API_KEY = os.getenv("WHISPER_API_KEY", "your_whisper_api_key")
    ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY", "your_assemblyai_api_key")
    
    # Model paths
    SENTIMENT_MODEL_PATH = os.getenv("SENTIMENT_MODEL_PATH", "path/to/sentiment/model")
    
    # Audio processing settings
    AUDIO_SAMPLE_RATE = 16000
    AUDIO_FORMAT = "wav"  # or "mp3"
    
    # Engagement score weights
    ENGAGEMENT_SCORE_WEIGHTS = {
        "tone_pitch": 0.5,
        "loudness": 0.3,
        "sentiment": 0.2
    }