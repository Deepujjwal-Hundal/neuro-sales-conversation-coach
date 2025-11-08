from flask import Blueprint, request, jsonify
from src.transcribe import transcribe_audio
from src.diarize import diarize_audio
from src.features import extract_features
from src.sentiment import analyze_sentiment
from src.engagement import compute_engagement_score
from src.video_utils import is_video_file, extract_audio_from_video
import os
import tempfile

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Create temp directory if it doesn't exist
    temp_dir = 'temp'
    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    # Save the uploaded file
    uploaded_file_path = os.path.join(temp_dir, file.filename)
    file.save(uploaded_file_path)

    # Check if it's a video file and extract audio if needed
    audio_path = uploaded_file_path
    is_video = is_video_file(file.filename)
    extracted_audio_path = None

    try:
        if is_video:
            # Extract audio from video
            print(f"Detected video file: {file.filename}. Extracting audio...")
            extracted_audio_path = os.path.join(temp_dir, f"{os.path.splitext(file.filename)[0]}_audio.wav")
            audio_path = extract_audio_from_video(uploaded_file_path, extracted_audio_path)
            print(f"Audio extracted to: {audio_path}")

        # Transcribe the audio
        transcription_segments = transcribe_audio(audio_path)
        
        # Format transcript and timestamps
        transcript = " ".join([seg.get('text', '') for seg in transcription_segments])
        timestamps = transcription_segments

        # Diarize the audio
        speaker_segments = diarize_audio(audio_path)

        # Extract features
        features = extract_features(audio_path)

        # Analyze sentiment
        sentiment_results = analyze_sentiment(transcript)
        
        # Calculate overall engagement score from features and sentiment
        # This is a simplified version - you may want to enhance this
        sentiment_score = 0.5
        if isinstance(sentiment_results, list) and len(sentiment_results) > 0:
            # Get average sentiment score
            if isinstance(sentiment_results[0], dict) and 'score' in sentiment_results[0]:
                sentiment_score = sum(r.get('score', 0.5) for r in sentiment_results) / len(sentiment_results)
        
        # Calculate engagement score
        engagement_score_value = (
            0.5 * features.get('pitch_variation', 0) +
            0.3 * features.get('avg_loudness', 0) +
            0.2 * sentiment_score
        )

        # Prepare response
        response = {
            'transcript': transcript,
            'timestamps': timestamps,
            'speaker_segments': speaker_segments,
            'features': features,
            'sentiment': sentiment_results,
            'engagement_score': engagement_score_value,
            'file_type': 'video' if is_video else 'audio',
            'original_filename': file.filename
        }

        return jsonify(response), 200

    except Exception as e:
        error_msg = str(e)
        print(f"Error processing file: {error_msg}")
        return jsonify({'error': f'Error processing file: {error_msg}'}), 500
    
    finally:
        # Clean up extracted audio file if it was created
        if extracted_audio_path and os.path.exists(extracted_audio_path):
            try:
                os.remove(extracted_audio_path)
            except:
                pass