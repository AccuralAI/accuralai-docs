# AccuralAI Documentation

This directory contains the Sphinx documentation for all AccuralAI packages.

## Quick Start

### Build Documentation

**Linux/macOS:**
```bash
cd docs
chmod +x build.sh
./build.sh
```

**Windows:**
```cmd
cd docs
build.bat
```

### Development Server

**Linux/macOS:**
```bash
cd docs
chmod +x serve.sh
./serve.sh
```

**Windows:**
```cmd
cd docs
serve.bat
```

The development server will automatically rebuild the documentation when files change and serve it at `http://localhost:8000`.

## Structure

- `conf.py` - Sphinx configuration
- `index.rst` - Main documentation index
- `requirements.txt` - Python dependencies for documentation
- `packages/` - Package-specific documentation
- `_build/` - Generated documentation (created after build)
- `_static/` - Static assets (CSS, images, etc.)
- `_templates/` - Custom Sphinx templates

## Package Documentation

Each package has its own documentation directory under `packages/`:

- `accuralai-core/` - Core orchestration package
- `accuralai-cache/` - Caching providers
- `accuralai-canonicalize/` - Canonicalization helpers
- `accuralai-google/` - Google Gemini backend
- `accuralai-ollama/` - Ollama backend
- `accuralai-router/` - Routing strategies
- `accuralai-validator/` - Validation plugins

## Features

- **Auto-generated API docs** using Sphinx autodoc
- **Cross-references** between packages
- **Search functionality** 
- **Responsive design** with Read the Docs theme
- **MyST Markdown support** for rich content
- **Intersphinx mapping** to external documentation

## Configuration

The documentation is configured in `conf.py` with:

- Auto-discovery of all packages
- Mock imports for external dependencies
- Intersphinx mapping to Python, Pydantic, AnyIO, and Click docs
- Napoleon extension for Google/NumPy docstrings
- MyST parser for Markdown support

## Adding New Packages

To add documentation for a new package:

1. Create a directory under `packages/your-package-name/`
2. Add an `index.rst` file with package overview
3. Create `.rst` files for each module using `automodule` directives
4. Update the main `index.rst` to include the new package

## Troubleshooting

### Import Errors

If you get import errors during build, check that:
- All packages are installed in development mode
- Mock imports are configured in `conf.py`
- Python path includes the packages directory

### Missing Documentation

If some modules aren't documented:
- Check that the module has proper docstrings
- Verify the `automodule` directive is correct
- Ensure the module is importable

### Build Errors

Common build errors:
- Missing dependencies: Install from `requirements.txt`
- Path issues: Ensure you're in the `docs/` directory
- Permission errors: Make scripts executable (`chmod +x *.sh`)
