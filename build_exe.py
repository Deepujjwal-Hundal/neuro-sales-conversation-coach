"""
Build script to create an .exe file for Neuro-Sales Conversation Coach
This script:
1. Builds the React frontend
2. Packages everything with PyInstaller
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, cwd=None, check=True):
    """Run a shell command and return the result"""
    print(f"Running: {command}")
    if cwd:
        print(f"Working directory: {cwd}")
    
    result = subprocess.run(
        command,
        shell=True,
        cwd=cwd,
        check=False,  # Don't raise exception, handle it manually
        capture_output=True,
        text=True
    )
    
    # Print output
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    
    # Check return code if check=True
    if check and result.returncode != 0:
        print(f"\n❌ Command failed with exit code {result.returncode}")
        print(f"Command: {command}")
        if result.stderr:
            print(f"Error output:\n{result.stderr}")
        raise subprocess.CalledProcessError(result.returncode, command, result.stdout, result.stderr)
    
    return result

def build_react_frontend():
    """Build the React frontend"""
    print("\n" + "="*60)
    print("Step 1: Building React Frontend")
    print("="*60)
    
    frontend_dir = Path(__file__).parent / "frontend" / "react-app"
    
    if not frontend_dir.exists():
        print(f"Error: Frontend directory not found at {frontend_dir}")
        return False
    
    # Check if npm is available
    try:
        npm_check = subprocess.run("npm --version", shell=True, capture_output=True, text=True)
        if npm_check.returncode != 0:
            print("Error: npm is not installed or not in PATH")
            return False
        print(f"Using npm version: {npm_check.stdout.strip()}")
    except Exception as e:
        print(f"Error checking npm: {e}")
        return False
    
    # Check if node_modules exists, if not, install dependencies
    package_json = frontend_dir / "package.json"
    if not package_json.exists():
        print(f"Error: package.json not found at {package_json}")
        return False
    
    if not (frontend_dir / "node_modules").exists():
        print("Installing npm dependencies...")
        print("This may take a few minutes...")
        try:
            result = run_command("npm install", cwd=str(frontend_dir), check=True)
            print("✓ Dependencies installed successfully")
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Failed to install npm dependencies")
            print(f"Exit code: {e.returncode}")
            if e.stdout:
                print(f"Output: {e.stdout}")
            if e.stderr:
                print(f"Error: {e.stderr}")
            print("\nPlease try running 'npm install' manually in the frontend/react-app directory")
            print("Then run this build script again.")
            return False
    else:
        print("✓ Dependencies already installed")
    
    # Build React app
    print("\nBuilding React app...")
    print("=" * 60)
    try:
        # Run build without capturing output so we can see real-time errors
        result = subprocess.run(
            "npm run build",
            shell=True,
            cwd=str(frontend_dir),
            check=False  # Don't raise exception yet
        )
        
        if result.returncode != 0:
            print("\n" + "=" * 60)
            print("❌ React build failed!")
            print(f"Exit code: {result.returncode}")
            print("\nCommon issues:")
            print("1. Missing dependencies - try running 'npm install' in frontend/react-app")
            print("2. Syntax errors in React code")
            print("3. Missing environment variables")
            print("\nTo debug, try running 'npm run build' manually in the frontend/react-app directory")
            print("=" * 60)
            return False
    except Exception as e:
        print(f"\n❌ Error running npm build: {e}")
        return False
    
    build_dir = frontend_dir / "build"
    if not build_dir.exists():
        print("Error: React build failed - build directory not found")
        return False
    
    print("✓ React frontend built successfully")
    return True

def build_exe():
    """Build the .exe using PyInstaller"""
    print("\n" + "="*60)
    print("Step 2: Building .exe with PyInstaller")
    print("="*60)
    
    backend_dir = Path(__file__).parent / "backend"
    spec_file = backend_dir / "build_exe.spec"
    
    if not spec_file.exists():
        print(f"Error: Spec file not found at {spec_file}")
        return False
    
    # Run PyInstaller
    print("Running PyInstaller...")
    run_command(f'pyinstaller "{spec_file}" --clean --noconfirm', cwd=str(backend_dir))
    
    # Check if exe was created
    dist_dir = backend_dir / "dist"
    exe_file = dist_dir / "NeuroSalesCoach.exe"
    
    if exe_file.exists():
        print(f"\n✓ .exe file created successfully at: {exe_file}")
        print(f"\nYou can find the executable in: {dist_dir}")
        return True
    else:
        print("Error: .exe file not found after build")
        return False

def main():
    """Main build process"""
    print("="*60)
    print("Neuro-Sales Conversation Coach - .exe Builder")
    print("="*60)
    
    # Check if we're in the right directory
    if not Path(__file__).parent.name == "neuro-sales-conversation-coach":
        print("Warning: This script should be run from the project root")
    
    # Step 1: Build React frontend
    if not build_react_frontend():
        print("\n❌ Build failed at React frontend step")
        sys.exit(1)
    
    # Step 2: Build .exe
    if not build_exe():
        print("\n❌ Build failed at .exe creation step")
        sys.exit(1)
    
    print("\n" + "="*60)
    print("✓ Build completed successfully!")
    print("="*60)
    print("\nThe .exe file is ready to use.")
    print("Note: The first run may take longer as models are loaded.")

if __name__ == "__main__":
    main()

