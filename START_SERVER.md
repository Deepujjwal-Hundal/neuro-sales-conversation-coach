# How to Start the Server

## Quick Start (Easiest Method)

### Option 1: Using Batch File (Recommended for Windows)
Double-click `run_server.bat` in the project root, or run:
```bash
run_server.bat
```

### Option 2: Using PowerShell Script
```powershell
powershell -ExecutionPolicy Bypass -File run_server.ps1
```

### Option 3: Manual Start
1. Open a terminal in the project root
2. Activate virtual environment (if using one):
   ```bash
   .venv\Scripts\activate
   ```
3. Navigate to backend:
   ```bash
   cd backend
   ```
4. Run the launcher:
   ```bash
   python launch.py
   ```

## Troubleshooting

### PowerShell Execution Policy Error
If you see "execution of scripts is disabled", use one of these:

**Method 1:** Use the batch file (`run_server.bat`) instead

**Method 2:** Bypass for this session:
```powershell
powershell -ExecutionPolicy Bypass -File run_server.ps1
```

**Method 3:** Change execution policy (requires admin):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Whisper Model Loading Error
If you see errors about Whisper:

1. **Reinstall Whisper:**
   ```bash
   pip uninstall openai-whisper
   pip install openai-whisper
   ```

2. **Install PyTorch (if needed):**
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
   ```

3. **The model now loads lazily** - it will only load when you actually upload a file, so the server should start even if there are initial issues.

### Frontend Not Built
If you see "Frontend Not Built" message:

1. Navigate to frontend:
   ```bash
   cd frontend/react-app
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Build the frontend:
   ```bash
   npm run build
   ```

4. Restart the server

## Accessing the Application

Once the server starts, open your browser and go to:
- **Main Application:** http://127.0.0.1:5000
- **API Endpoint:** http://127.0.0.1:5000/api/upload

The browser should open automatically when using `launch.py`.

