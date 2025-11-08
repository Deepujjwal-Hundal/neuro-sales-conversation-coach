# Building .exe Application

This guide explains how to build a standalone .exe file for the Neuro-Sales Conversation Coach application.

## Prerequisites

1. **Python 3.8+** installed on Windows
2. **Node.js and npm** installed (for building the React frontend)
3. All Python dependencies installed (see Installation section)

## Installation Steps

### 1. Install Python Dependencies

Navigate to the `backend` directory and install all required packages:

```bash
cd backend
pip install -r requirements.txt
```

### 2. Install Node.js Dependencies

Navigate to the `frontend/react-app` directory and install npm packages:

```bash
cd ../frontend/react-app
npm install
```

### 3. Build the .exe

From the project root directory, run the build script:

```bash
cd ../..
python build_exe.py
```

The build script will:
1. Build the React frontend (creates static files)
2. Package everything with PyInstaller into a single .exe file

## Output

After successful build, you'll find:
- **Executable**: `backend/dist/NeuroSalesCoach.exe`
- **Distribution folder**: `backend/dist/` (contains the .exe and required files)

## Running the .exe

1. Navigate to `backend/dist/`
2. Double-click `NeuroSalesCoach.exe`
3. The application will start a local server
4. Open your browser and go to `http://127.0.0.1:5000`

## Manual Build (Alternative)

If you prefer to build manually:

### Step 1: Build React Frontend
```bash
cd frontend/react-app
npm run build
```

### Step 2: Build .exe with PyInstaller
```bash
cd ../../backend
pyinstaller build_exe.spec --clean --noconfirm
```

## Troubleshooting

### Issue: "Module not found" errors
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Some packages (like transformers, torch) may need additional data files

### Issue: React build fails
- Ensure Node.js and npm are installed
- Run `npm install` in `frontend/react-app` first
- Check that you have internet connection for downloading packages

### Issue: Large .exe file size
- This is normal due to included ML models (Whisper, transformers, torch)
- The .exe may be 500MB-2GB depending on included models
- Consider using UPX compression (already enabled in spec file)

### Issue: Application doesn't start
- Check if port 5000 is already in use
- Try running from command line to see error messages
- Ensure all required model files are included

### Issue: Frontend not loading
- Verify that `frontend/react-app/build` directory exists after React build
- Check that the build directory is included in PyInstaller spec file

## Notes

- **First Run**: The first time you run the .exe, it may take longer as models are loaded
- **Console Window**: The .exe runs with a console window by default. To hide it, set `console=False` in `build_exe.spec`
- **Port**: The application runs on `http://127.0.0.1:5000` by default
- **Temp Files**: Uploaded audio files are temporarily stored in a `temp` directory

## Customization

### Change Port
Edit `backend/app.py` and change the port number:
```python
app.run(host='127.0.0.1', port=5000, debug=False)
```

### Hide Console Window
Edit `backend/build_exe.spec` and change:
```python
console=False,  # Hide console window
```

### Add Icon
1. Create or obtain an `.ico` file
2. Edit `backend/build_exe.spec` and set:
```python
icon='path/to/your/icon.ico',
```

## Distribution

To distribute the application:
1. Copy the entire `backend/dist` folder
2. Include a README with usage instructions
3. Note: Users don't need Python or Node.js installed to run the .exe

