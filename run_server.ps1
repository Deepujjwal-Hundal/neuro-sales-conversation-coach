# PowerShell script to run the Flask server
# Run with: powershell -ExecutionPolicy Bypass -File run_server.ps1

Write-Host "Starting Neuro-Sales Conversation Coach..." -ForegroundColor Green
Write-Host ""

# Activate virtual environment
if (Test-Path ".venv\Scripts\Activate.ps1") {
    & ".venv\Scripts\Activate.ps1"
} else {
    Write-Host "Warning: Virtual environment not found at .venv" -ForegroundColor Yellow
    Write-Host "Continuing without virtual environment..." -ForegroundColor Yellow
}

# Change to backend directory and run
Set-Location "neuro-sales-conversation-coach\backend"
python launch.py

