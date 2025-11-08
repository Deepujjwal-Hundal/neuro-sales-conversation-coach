# Video File Support

The Neuro-Sales Conversation Coach now supports both video and audio file uploads!

## Supported Formats

### Video Formats
- MP4, AVI, MOV, MKV, FLV, WMV, WebM, M4V, 3GP

### Audio Formats
- WAV, MP3, M4A, OGG

## Installation Requirements

### FFmpeg (Required for Video Processing)

FFmpeg is required to extract audio from video files. It's not a Python package, so it needs to be installed separately.

#### Windows Installation

1. **Download FFmpeg:**
   - Visit: https://ffmpeg.org/download.html
   - Or use: https://www.gyan.dev/ffmpeg/builds/
   - Download the "ffmpeg-release-essentials.zip"

2. **Extract and Install:**
   - Extract the zip file to a location like `C:\ffmpeg`
   - Add `C:\ffmpeg\bin` to your system PATH:
     - Open "Environment Variables" in Windows
     - Edit the "Path" variable
     - Add `C:\ffmpeg\bin`
     - Restart your terminal/IDE

3. **Verify Installation:**
   ```bash
   ffmpeg -version
   ```

#### macOS Installation

```bash
# Using Homebrew
brew install ffmpeg
```

#### Linux Installation

```bash
# Ubuntu/Debian
sudo apt-get update
sudo apt-get install ffmpeg

# Fedora
sudo dnf install ffmpeg

# Arch Linux
sudo pacman -S ffmpeg
```

## How It Works

1. **Upload**: User selects a video or audio file from their device
2. **Detection**: Backend detects if the file is a video
3. **Extraction**: If video, FFmpeg extracts the audio track
4. **Processing**: The extracted audio is processed normally (transcription, analysis, etc.)
5. **Results**: Same analysis results as audio files

## Features

- **Drag & Drop**: Easy file selection with drag-and-drop support
- **File Preview**: Preview video/audio before uploading
- **Automatic Detection**: Automatically detects video vs audio files
- **Seamless Processing**: Video files are processed the same way as audio files

## Troubleshooting

### Error: "FFmpeg not found"

**Solution**: Install FFmpeg and ensure it's in your system PATH. See installation instructions above.

### Error: "FFmpeg error: [error message]"

**Possible causes:**
- Corrupted video file
- Unsupported video codec
- Insufficient disk space for temporary files

**Solution**: 
- Try converting the video to MP4 format
- Check available disk space
- Verify the video file plays in a media player

### Large Video Files

Large video files may take longer to process:
- Audio extraction time depends on video length
- Processing time increases with file size
- Consider compressing videos before upload

## Technical Details

- Audio is extracted at 16kHz sample rate (optimal for speech)
- Mono channel audio (reduces file size)
- PCM 16-bit audio format
- Temporary audio files are automatically cleaned up after processing

