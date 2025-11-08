# Neuro-Sales Conversation Coach

## Overview
The Neuro-Sales Conversation Coach is a web application designed to analyze sales calls and provide insights to improve sales conversations. The application transcribes audio recordings, performs speaker diarization, analyzes vocal tone characteristics, and computes an engagement score to help users enhance their persuasive effectiveness.

## Features
- **Video & Audio Upload**: Users can upload video or audio recordings of sales calls (MP4, AVI, MOV, WAV, MP3, and more).
- **Drag & Drop Interface**: Modern, user-friendly file selection with drag-and-drop support and file preview.
- **Transcription**: The application transcribes the audio with timestamps and separates speakers.
- **Vocal Tone Analysis**: It detects pitch variation, speech rate, and loudness dynamics.
- **Sentiment Analysis**: The app performs sentiment and emotion analysis on the transcribed text.
- **Engagement Scoring**: An engagement score is calculated based on tone, loudness, and sentiment.
- **Visualizations**: Users can view a color-coded transcript, engagement timeline graph, and highlighted moments of interest.
- **Improvement Suggestions**: The app provides actionable suggestions to enhance sales conversation patterns.

## Technical Stack
- **Backend**: Python with Flask
- **Transcription**: Whisper or AssemblyAI
- **Speaker Diarization**: pyannote-audio
- **Audio Feature Extraction**: librosa
- **Sentiment Analysis**: HuggingFace models
- **Frontend**: React or Streamlit

## Installation Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd neuro-sales-conversation-coach
   ```

2. Set up the backend:
   - Navigate to the `backend` directory.
   - Install dependencies:
     ```
     pip install -r requirements.txt
     ```
   - **Install FFmpeg** (required for video file support):
     - See [VIDEO_SUPPORT.md](VIDEO_SUPPORT.md) for detailed installation instructions
     - Windows: Download from https://ffmpeg.org/download.html and add to PATH
     - macOS: `brew install ffmpeg`
     - Linux: `sudo apt-get install ffmpeg` (Ubuntu/Debian)

3. (Optional) Build and run the Docker container:
   ```
   docker build -t neuro-sales-coach-backend .
   docker run -p 5000:5000 neuro-sales-coach-backend
   ```

4. Set up the frontend:
   - Navigate to the `frontend/react-app` directory.
   - Install dependencies:
     ```
     npm install
     ```

5. Start the frontend application:
   ```
   npm start
   ```

## Usage
- Upload an audio file on the upload page.
- View the transcribed text, engagement score, and suggestions on the results page.

## Building Standalone .exe Application

To create a standalone Windows executable (.exe) file for easier distribution:

1. **Install Prerequisites**:
   - Ensure Python 3.8+ and Node.js are installed
   - Install Python dependencies: `cd backend && pip install -r requirements.txt`
   - Install Node.js dependencies: `cd frontend/react-app && npm install`

2. **Build the .exe**:
   ```bash
   python build_exe.py
   ```

3. **Run the .exe**:
   - Navigate to `backend/dist/`
   - Double-click `NeuroSalesCoach.exe`
   - The application will automatically open in your browser

For detailed build instructions and troubleshooting, see [BUILD_EXE_INSTRUCTIONS.md](BUILD_EXE_INSTRUCTIONS.md).

## Example Audio
An example audio file is included in the `example_audio` directory for testing purposes.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License.