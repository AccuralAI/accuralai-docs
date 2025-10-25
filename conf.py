# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# Note: Packages are installed via pip on Read the Docs, so no manual path setup needed.
# For local development with editable installs, the packages are already on sys.path.

# -- Project information -----------------------------------------------------

project = 'AccuralAI'
copyright = '2024, AccuralAI Maintainers'
author = 'AccuralAI Maintainers'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'sphinx.ext.todo',
    'myst_parser',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Extension configuration -------------------------------------------------

# -- Options for autodoc -----------------------------------------------------
autodoc_default_options = {
    'members': True,
    'member-order': 'bysource',
    'special-members': '__init__',
    'undoc-members': False,  # Changed to False to avoid import issues
    'exclude-members': '__weakref__'
}

# Mock imports for packages that might not be available during doc build
autodoc_mock_imports = [
    'anyio',
    'pydantic',
    'click',
    'tomli',
    'pytest',
    'ruff',
    'google-genai',
    'httpx',
    'jsonschema',
]

# -- Options for autosummary -------------------------------------------------
autosummary_generate = True

# -- Options for napoleon ----------------------------------------------------
napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = False
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

# -- Options for intersphinx extension ---------------------------------------
intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'pydantic': ('https://docs.pydantic.dev/latest/', None),
    'anyio': ('https://anyio.readthedocs.io/en/stable/', None),
    'click': ('https://click.palletsprojects.com/en/stable/', None),
}

# -- Options for todo extension ----------------------------------------------
todo_include_todos = True

# -- Options for MyST Parser -------------------------------------------------
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "fieldlist",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "strikethrough",
    "substitution",
    "tasklist",
]

# -- Custom configuration ----------------------------------------------------

# Package information for documentation
packages_info = {
    'accuralai-core': {
        'description': 'Async orchestration nucleus for the AccuralAI local LLM ecosystem.',
        'path': 'accuralai_core',
        'entry_points': [
            'accuralai_core.backends',
            'accuralai_core.validators', 
            'accuralai_core.caches'
        ]
    },
    'accuralai-cache': {
        'description': 'Caching providers for the AccuralAI LLM pipeline.',
        'path': 'accuralai_cache',
        'entry_points': ['accuralai_core.caches']
    },
    'accuralai-canonicalize': {
        'description': 'Canonicalization helpers and plugins for the AccuralAI LLM pipeline.',
        'path': 'accuralai_canonicalize',
        'entry_points': ['accuralai_core.canonicalizers']
    },
    'accuralai-google': {
        'description': 'Google Gemini backend adapter for AccuralAI.',
        'path': 'accuralai_google',
        'entry_points': ['accuralai_core.backends']
    },
    'accuralai-ollama': {
        'description': 'Ollama backend adapter for AccuralAI.',
        'path': 'accuralai_ollama',
        'entry_points': ['accuralai_core.backends']
    },
    'accuralai-router': {
        'description': 'Routing strategies for AccuralAI LLM pipeline.',
        'path': 'accuralai_router',
        'entry_points': ['accuralai_core.routers']
    },
    'accuralai-validator': {
        'description': 'Validation plugins for AccuralAI LLM pipeline.',
        'path': 'accuralai_validator',
        'entry_points': ['accuralai_core.validators']
    }
}
