"""
Utility functions for video file processing
Extracts audio from video files for analysis
"""

import os
import subprocess
import tempfile
from pathlib import Path

def is_video_file(filename):
    """Check if the file is a video file based on extension"""
    video_extensions = {'.mp4', '.avi', '.mov', '.mkv', '.flv', '.wmv', '.webm', '.m4v', '.3gp'}
    file_ext = Path(filename).suffix.lower()
    return file_ext in video_extensions

def extract_audio_from_video(video_path, output_audio_path=None):
    """
    Extract audio from video file using ffmpeg
    
    Args:
        video_path: Path to the input video file
        output_audio_path: Optional path for output audio file. If None, creates a temp file.
    
    Returns:
        Path to the extracted audio file
    """
    try:
        # If no output path specified, create a temporary file
        if output_audio_path is None:
            temp_dir = tempfile.gettempdir()
            video_name = Path(video_path).stem
            output_audio_path = os.path.join(temp_dir, f"{video_name}_extracted_audio.wav")
        
        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_audio_path), exist_ok=True)
        
        # Use ffmpeg to extract audio
        # -i: input file
        # -vn: disable video
        # -acodec pcm_s16le: audio codec (PCM 16-bit)
        # -ar 16000: sample rate 16kHz (good for speech)
        # -ac 1: mono channel
        # -y: overwrite output file if exists
        command = [
            'ffmpeg',
            '-i', video_path,
            '-vn',  # No video
            '-acodec', 'pcm_s16le',  # PCM audio codec
            '-ar', '16000',  # Sample rate
            '-ac', '1',  # Mono
            '-y',  # Overwrite
            output_audio_path
        ]
        
        # Run ffmpeg command
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        
        if not os.path.exists(output_audio_path):
            raise Exception(f"Audio extraction failed: output file not created")
        
        return output_audio_path
    
    except subprocess.CalledProcessError as e:
        raise Exception(f"FFmpeg error: {e.stderr}")
    except FileNotFoundError:
        raise Exception("FFmpeg not found. Please install FFmpeg to process video files.")
    except Exception as e:
        raise Exception(f"Error extracting audio from video: {str(e)}")

def get_video_info(video_path):
    """
    Get basic information about the video file
    
    Returns:
        dict with video information
    """
    try:
        command = [
            'ffprobe',
            '-v', 'quiet',
            '-print_format', 'json',
            '-show_format',
            '-show_streams',
            video_path
        ]
        
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )
        
        import json
        info = json.loads(result.stdout)
        
        # Extract relevant information
        video_info = {
            'duration': None,
            'size': None,
            'format': None
        }
        
        if 'format' in info:
            format_info = info['format']
            video_info['duration'] = float(format_info.get('duration', 0))
            video_info['size'] = int(format_info.get('size', 0))
            video_info['format'] = format_info.get('format_name', 'unknown')
        
        return video_info
    
    except Exception as e:
        # Return default info if probe fails
        return {
            'duration': None,
            'size': os.path.getsize(video_path) if os.path.exists(video_path) else None,
            'format': Path(video_path).suffix
        }

