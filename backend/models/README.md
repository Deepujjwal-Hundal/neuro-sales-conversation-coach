# Contents of the file: /neuro-sales-conversation-coach/neuro-sales-conversation-coach/backend/models/README.md

# Neuro-Sales Conversation Coach Models Documentation

This directory contains the models used in the Neuro-Sales Conversation Coach application. The models are responsible for various tasks including transcription, speaker diarization, sentiment analysis, and engagement scoring.

## Models Overview

1. **Transcription Model**:
   - Utilizes Whisper or AssemblyAI for converting audio recordings into text.
   - Provides timestamps for each segment of the transcription.

2. **Speaker Diarization Model**:
   - Implements pyannote-audio to differentiate between speakers in the audio.
   - Outputs segments labeled with speaker identifiers (Speaker A and Speaker B).

3. **Sentiment Analysis Model**:
   - Leverages a HuggingFace sentiment model to analyze the emotional tone of the transcribed text.
   - Classifies segments into various sentiment categories (positive, negative, neutral).

4. **Engagement Scoring Model**:
   - Computes an engagement score based on vocal tone characteristics, loudness dynamics, and sentiment analysis.
   - The scoring formula is as follows:
     - 50% from tone and pitch change
     - 30% from loudness dynamics
     - 20% from sentiment/emotional polarity

## Usage

The models are integrated into the backend of the application and are invoked during the processing of uploaded audio files. The results are then presented to the user through the frontend interface.

## Future Improvements

- Explore additional models for enhanced sentiment analysis.
- Implement more sophisticated engagement scoring algorithms.
- Consider adding support for more audio formats and languages.