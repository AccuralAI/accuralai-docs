AccuralAI Ollama
=================

Ollama backend adapter for AccuralAI.

Overview
--------

``accuralai-ollama`` provides integration with local Ollama instances through the HTTP API.

Key Features
------------

* **Local LLM Support**: Integration with Ollama's local model serving
* **Streaming Support**: Handles newline-delimited streaming responses
* **Usage Metrics**: Converts Ollama metrics to AccuralAI contracts
* **Model Management**: Support for different Ollama models

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

   from accuralai_ollama.backend import build_ollama_backend

   backend = build_ollama_backend(
       base_url="http://localhost:11434",
       model="llama2"
   )

   response = await backend.generate({
       "prompt": "Hello, world!",
       "temperature": 0.7,
       "max_tokens": 100
   })

With Custom Configuration
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   backend = build_ollama_backend(
       base_url="http://localhost:11434",
       model="codellama",
       options={
           "temperature": 0.7,
           "top_p": 0.9,
           "repeat_penalty": 1.1
       }
   )

Configuration
-------------

The Ollama backend connects to a local Ollama instance. Default configuration:

* **Base URL**: ``http://localhost:11434``
* **Model**: ``llama2`` (configurable)

Development
-----------

.. code-block:: bash

   # Install in development mode
   pip install -e packages/accuralai-ollama[dev]

   # Run tests
   pytest packages/accuralai-ollama/tests/
