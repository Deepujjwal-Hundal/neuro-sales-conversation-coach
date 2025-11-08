"""
Launcher script that starts the Flask app and opens the browser automatically
"""

import webbrowser
import threading
import time
from app import app

def open_browser():
    """Open the browser after a short delay"""
    time.sleep(1.5)  # Wait for server to start
    webbrowser.open('http://127.0.0.1:5000')

if __name__ == "__main__":
    # Start browser in a separate thread
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Start Flask app
    print("Starting Neuro-Sales Conversation Coach...")
    print("Opening browser at http://127.0.0.1:5000")
    print("Press Ctrl+C to stop the server")
    app.run(host='127.0.0.1', port=5000, debug=False)

