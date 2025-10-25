AccuralAI Canonicalize
======================

Canonicalization helpers and plugins for the AccuralAI LLM pipeline.

Overview
--------

``accuralai-canonicalize`` exposes canonicalization plugins that standardize input processing:

* **Standard Canonicalizer**: Trims prompt whitespace, applies templates, normalizes tags
* **Advanced Canonicalizer**: Additional processing with configurable metadata injection

Key Features
------------

* **Prompt Normalization**: Consistent whitespace and formatting
* **Template Application**: Optional prompt templating
* **Tag Management**: Normalization and deduplication of metadata tags
* **Cache Key Generation**: Deterministic keys from configurable metadata fields

API Reference
-------------

.. toctree::
   :maxdepth: 2

   canonicalizer

Usage Examples
--------------

Standard Canonicalizer
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from accuralai_canonicalize.canonicalizer import build_standard_canonicalizer

   canonicalizer = build_standard_canonicalizer(
       trim_whitespace=True,
       apply_templates=True,
       normalize_tags=True
   )

   result = await canonicalizer.canonicalize({
       "prompt": "  Hello, world!  ",
       "tags": ["test", "demo", "TEST"],
       "metadata": {"user": "developer"}
   })

Advanced Canonicalizer
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from accuralai_canonicalize.canonicalizer import build_advanced_canonicalizer

   canonicalizer = build_advanced_canonicalizer(
       template_config={
           "system_template": "You are a helpful assistant: {prompt}",
           "user_template": "User: {prompt}"
       },
       metadata_defaults={
           "model": "default",
           "temperature": 0.7
       }
   )

   result = await canonicalizer.canonicalize({
       "prompt": "Hello",
       "role": "user"
   })

Configuration
-------------

Canonicalizers are registered as entry points under ``accuralai_core.canonicalizers``:

* ``standard``: Basic canonicalization with trimming and normalization
* ``advanced``: Extended canonicalization with templating and metadata injection

Development
-----------

.. code-block:: bash

   # Install in development mode
   pip install -e packages/accuralai-canonicalize[dev]

   # Run tests
   pytest packages/accuralai-canonicalize/tests/
