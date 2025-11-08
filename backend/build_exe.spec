# -*- mode: python ; coding: utf-8 -*-

import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Get the base directory (where this spec file is located)
base_dir = os.path.dirname(os.path.abspath(SPECNAME))

# Collect data files for various packages
datas = []

# Collect React frontend build files
frontend_build = os.path.join(base_dir, '..', 'frontend', 'react-app', 'build')
if os.path.exists(frontend_build):
    # Add the entire build directory
    datas.append((frontend_build, 'frontend/react-app/build'))

# Collect example audio files
example_audio = os.path.join(base_dir, '..', 'example_audio')
if os.path.exists(example_audio):
    datas.append((example_audio, 'example_audio'))

# Collect data files for transformers, torch, whisper, etc.
try:
    datas += collect_data_files('transformers')
    datas += collect_data_files('torch')
    datas += collect_data_files('whisper')
except:
    pass

# Hidden imports for packages that PyInstaller might miss
hiddenimports = [
    'transformers',
    'torch',
    'whisper',
    'librosa',
    'pyannote.audio',
    'sklearn',
    'soundfile',
    'numpy',
    'pandas',
    'flask',
    'flask_cors',
]

# Collect submodules
hiddenimports += collect_submodules('transformers')
hiddenimports += collect_submodules('torch')
hiddenimports += collect_submodules('whisper')

a = Analysis(
    ['launch.py'],  # Use launch.py instead of app.py to auto-open browser
    pathex=[base_dir],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='NeuroSalesCoach',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,  # Set to False if you want a windowed app (no console)
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=None,  # You can add an icon file path here if you have one
)

