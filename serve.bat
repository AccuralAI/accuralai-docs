@echo off
REM AccuralAI Documentation Development Server for Windows
REM This script starts a development server that auto-rebuilds documentation on changes

setlocal enabledelayedexpansion

echo Starting AccuralAI Documentation Development Server...

REM Change to docs directory
cd /d "%~dp0"

REM Install requirements if not already installed
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing requirements...
pip install -r requirements.txt

REM Install all packages in development mode for autodoc
echo Installing packages in development mode...
pip install -e ..\packages\accuralai-core
pip install -e ..\packages\accuralai-cache
pip install -e ..\packages\accuralai-canonicalize
pip install -e ..\packages\accuralai-google
pip install -e ..\packages\accuralai-ollama
pip install -e ..\packages\accuralai-router
pip install -e ..\packages\accuralai-validator

REM Start development server
echo Starting development server...
echo Documentation will be available at http://localhost:8000
echo Press Ctrl+C to stop the server

sphinx-autobuild -b html . _build\html --host 0.0.0.0 --port 8000

pause
