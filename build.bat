@echo off
REM AccuralAI Documentation Build Script for Windows
REM This script builds the Sphinx documentation for all packages

setlocal enabledelayedexpansion

echo Building AccuralAI Documentation...

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

REM Clean previous builds
echo Cleaning previous builds...
if exist "_build" rmdir /s /q "_build"

REM Build documentation
echo Building documentation...
sphinx-build -b html . _build\html

echo Documentation built successfully!
echo Open _build\html\index.html in your browser to view the documentation.

pause
