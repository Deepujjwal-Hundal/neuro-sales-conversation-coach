from flask import Flask, send_from_directory
from flask_cors import CORS
from src.api import api_bp
import os
import sys

# Determine the base directory
# When running as .exe, use sys._MEIPASS (PyInstaller temp directory)
if getattr(sys, 'frozen', False):
    # Running as compiled .exe
    BASE_DIR = sys._MEIPASS
    FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, 'frontend', 'react-app', 'build')
else:
    # Running as script
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    FRONTEND_BUILD_DIR = os.path.join(BASE_DIR, '..', 'frontend', 'react-app', 'build')

app = Flask(__name__, static_folder=FRONTEND_BUILD_DIR, static_url_path='')

# Enable CORS for all routes
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Register the API blueprint
app.register_blueprint(api_bp)

# Serve React app for all non-API routes
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if not os.path.exists(FRONTEND_BUILD_DIR):
        return """
        <html>
            <head><title>Frontend Not Built</title></head>
            <body style="font-family: Arial; padding: 40px; text-align: center;">
                <h1>Frontend Not Built</h1>
                <p>The React frontend has not been built yet.</p>
                <p>Please run: <code>cd frontend/react-app && npm install && npm run build</code></p>
                <p>Or use the API directly at: <a href="/api/upload">/api/upload</a></p>
            </body>
        </html>
        """, 200
    
    if path != "" and os.path.exists(os.path.join(FRONTEND_BUILD_DIR, path)):
        return send_from_directory(FRONTEND_BUILD_DIR, path)
    else:
        return send_from_directory(FRONTEND_BUILD_DIR, 'index.html')

if __name__ == "__main__":
    # For production/exe, use host='127.0.0.1' and a fixed port
    app.run(host='127.0.0.1', port=5000, debug=False)