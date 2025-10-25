#!/bin/bash

# AccuralAI Documentation Build Script
# This script builds the Sphinx documentation for all packages

set -e

echo "Building AccuralAI Documentation..."

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

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf _build

# Build documentation
echo "Building documentation..."
sphinx-build -b html . _build/html

echo "Documentation built successfully!"
echo "Open _build/html/index.html in your browser to view the documentation."
