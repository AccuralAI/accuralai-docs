#!/bin/bash

# AccuralAI Documentation Development Server
# This script starts a development server that auto-rebuilds documentation on changes

set -e

echo "Starting AccuralAI Documentation Development Server..."

# Change to docs directory
cd "$(dirname "$0")"

# Install requirements if not already installed
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate || source venv/Scripts/activate

echo "Installing requirements..."
pip install -r requirements.txt

# Install all packages in development mode for autodoc
echo "Installing packages in development mode..."
pip install -e ../packages/accuralai-core
pip install -e ../packages/accuralai-cache
pip install -e ../packages/accuralai-canonicalize
pip install -e ../packages/accuralai-google
pip install -e ../packages/accuralai-ollama
pip install -e ../packages/accuralai-router
pip install -e ../packages/accuralai-validator

# Start development server
echo "Starting development server..."
echo "Documentation will be available at http://localhost:8000"
echo "Press Ctrl+C to stop the server"

sphinx-autobuild -b html . _build/html --host 0.0.0.0 --port 8000
