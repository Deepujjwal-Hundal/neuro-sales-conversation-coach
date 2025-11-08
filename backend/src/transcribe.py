import os
import json

# Lazy load model to avoid import-time errors
_model = None

def get_model():
    """Lazy load the Whisper model"""
    global _model
    if _model is None:
        try:
            from whisper import load_model
            print("Loading Whisper model (this may take a moment)...")
            _model = load_model("base")
            print("Whisper model loaded successfully")
        except Exception as e:
            error_msg = f"Failed to load Whisper model: {str(e)}"
            print(f"Error: {error_msg}")
            print("\nTroubleshooting:")
            print("1. Make sure you have installed: pip install openai-whisper")
            print("2. On Windows, you may need: pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu")
            print("3. Try reinstalling whisper: pip uninstall openai-whisper && pip install openai-whisper")
            raise Exception(error_msg)
    return _model

def transcribe_audio(file_path):
    """Transcribe audio file using Whisper"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")
    
    try:
        model = get_model()
        result = model.transcribe(file_path, word_timestamps=True)
        
        # Prepare the transcription with timestamps
        transcription = []
        for segment in result['segments']:
            transcription.append({
                "start": segment['start'],
                "end": segment['end'],
                "text": segment['text']
            })
        
        return transcription
    except Exception as e:
        error_msg = f"Transcription failed: {str(e)}"
        print(f"Error: {error_msg}")
        raise Exception(error_msg)

def save_transcription(transcription, output_path):
    with open(output_path, 'w') as f:
        json.dump(transcription, f, indent=4)

def main():
    audio_file = "path/to/audio/file.wav"  # Replace with actual audio file path
    output_file = "transcription.json"  # Output file for transcription
    
    transcription = transcribe_audio(audio_file)
    save_transcription(transcription, output_file)
    print(f"Transcription saved to {output_file}")

if __name__ == "__main__":
    main()