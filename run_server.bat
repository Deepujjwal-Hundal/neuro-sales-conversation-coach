@echo off
REM Batch file to run the Flask server (bypasses PowerShell execution policy)
echo Starting Neuro-Sales Conversation Coach...
echo.

REM Activate virtual environment
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
) else (
    echo Warning: Virtual environment not found at .venv
    echo Continuing without virtual environment...
)

REM Change to backend directory and run
cd neuro-sales-conversation-coach\backend
python launch.py

pause

