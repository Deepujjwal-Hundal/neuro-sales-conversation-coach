def extract_audio_features(audio_file):
    import librosa
    import numpy as np

    # Load the audio file
    y, sr = librosa.load(audio_file, sr=None)

    # Extract pitch (fundamental frequency)
    pitches, magnitudes = librosa.piptrack(y=y, sr=sr)
    pitch_variation = np.mean(pitches[pitches > 0]) if np.any(pitches > 0) else 0.0

    # Extract loudness
    loudness = librosa.feature.rms(y=y)
    avg_loudness = np.mean(loudness) if len(loudness) > 0 else 0.0

    # Extract speech rate (words per minute)
    # This is a placeholder; actual implementation would require transcription
    speech_rate = estimate_speech_rate(audio_file)

    return {
        'pitch_variation': float(pitch_variation),
        'avg_loudness': float(avg_loudness),
        'speech_rate': speech_rate
    }

# Alias for compatibility
extract_features = extract_audio_features

def estimate_speech_rate(audio_file):
    # Placeholder function for estimating speech rate
    # Actual implementation would involve counting words in the transcription
    return 150  # Assume an average speech rate of 150 words per minute

def compute_engagement_score(features):
    tone_weight = 0.5
    loudness_weight = 0.3
    sentiment_weight = 0.2

    # Placeholder for sentiment score; actual implementation would analyze sentiment
    sentiment_score = 0.5  

    engagement_score = (
        tone_weight * features['pitch_variation'] +
        loudness_weight * features['avg_loudness'] +
        sentiment_weight * sentiment_score
    )

    return engagement_score