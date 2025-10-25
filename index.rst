AccuralAI Documentation
========================

Welcome to the AccuralAI documentation! This documentation covers all packages in the AccuralAI ecosystem.

Quick Start
-----------

AccuralAI ships pragmatic tooling that compounds small wins into observable LLM quality improvements. Every package in this monorepo is a building block for evaluating, routing, or operationalizing existing models rather than training new ones.

Packages Overview
-----------------

Core Packages
~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :caption: Core Packages

   packages/accuralai-core/index
   packages/accuralai-cache/index
   packages/accuralai-canonicalize/index

Backend Adapters
~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :caption: Backend Adapters

   packages/accuralai-google/index
   packages/accuralai-ollama/index

Plugins & Extensions
~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2
   :caption: Plugins & Extensions

   packages/accuralai-router/index
   packages/accuralai-validator/index

Installation
------------

Install the complete AccuralAI ecosystem:

.. code-block:: bash

   pip install accuralai

Or install individual packages:

.. code-block:: bash

   pip install accuralai-core
   pip install accuralai-cache
   pip install accuralai-canonicalize
   # ... etc

Philosophy
----------

AccuralAI focuses on:

* **Pragmatic tooling** that compounds small wins
* **Observable improvements** in LLM quality
* **Building blocks** for evaluation, routing, and operationalization
* **Research alongside production** code

Getting Started
---------------

1. **Core Orchestration**: Start with ``accuralai-core`` to understand the pipeline architecture
2. **Caching**: Add ``accuralai-cache`` for production-ready caching
3. **Backends**: Choose your LLM provider with ``accuralai-google`` or ``accuralai-ollama``
4. **Routing**: Implement intelligent routing with ``accuralai-router``
5. **Validation**: Add content validation with ``accuralai-validator``

Configuration
-------------

See the `configuration example <../plan/accuralai-core-config-example.toml>`_ for a complete setup.

Contributing
------------

Research and docs live alongside production code so contributors can trace ideas from ``plan/`` into shipped modules.

License
-------

Apache-2.0 License - see individual package licenses for details.
