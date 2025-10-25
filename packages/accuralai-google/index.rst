AccuralAI Google
================

Google Gemini backend adapter for AccuralAI.

Overview
--------

``accuralai-google`` provides integration with Google's Gemini API through the ``google-genai`` SDK.

Key Features
------------

* **Gemini Integration**: Full support for Google's Gemini models
* **Streaming Support**: Handles streaming responses
* **Usage Metrics**: Maps Google's usage data to AccuralAI contracts
* **Safety Metadata**: Preserves safety ratings and filtering information

API Reference
-------------

.. toctree::
   :maxdepth: 2

   backend

Usage Examples
--------------

Basic Usage
~~~~~~~~~~~

.. code-block:: python

   from accuralai_google.backend import build_google_backend

   backend = build_google_backend(
       api_key="your-api-key",
       model="gemini-pro"
   )

   response = await backend.generate({
       "prompt": "Hello, world!",
       "temperature": 0.7,
       "max_tokens": 100
   })

With Configuration
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   backend = build_google_backend(
       api_key="your-api-key",
       model="gemini-pro",
       generation_config={
           "temperature": 0.7,
           "max_output_tokens": 100,
           "top_p": 0.9
       }
   )

Configuration
-------------

The Google backend requires an API key, which can be provided via:

1. Configuration file
2. ``GOOGLE_GENAI_API_KEY`` environment variable

Development
-----------

.. code-block:: bash

   # Install in development mode
   pip install -e packages/accuralai-google[dev]

   # Run tests
   pytest packages/accuralai-google/tests/
