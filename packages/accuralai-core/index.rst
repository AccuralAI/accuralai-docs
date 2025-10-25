AccuralAI Core
==============

The orchestration nucleus for the AccuralAI local LLM ecosystem.

Overview
--------

``accuralai-core`` provides the async stage runner that orchestrates the entire LLM pipeline. Requests flow through:

1. **Canonicalization** → Cache lookup → Router selection → Backend invocation → Validation → Optional post-processing

Stage metadata is recorded on an ``ExecutionContext`` for tracing, cancellation, and event publishing.

Key Components
--------------

Pipeline Architecture
~~~~~~~~~~~~~~~~~~~~~~

The core pipeline (``accuralai_core.core.pipeline``) defines the async stage runner that processes requests through canonical stages.

Context Management
~~~~~~~~~~~~~~~~~~

``ExecutionContext`` (``accuralai_core.core.context``) provides tracing, cancellation, and event publishing capabilities.

Plugin System
~~~~~~~~~~~~~

Plugin groups follow the ``accuralai_core.<stage>`` naming convention and are auto-discovered via importlib entry points.

API Reference
-------------

.. toctree::
   :maxdepth: 2

   core/pipeline
   core/context
   core/orchestrator
   core/instrumentation
   core/events
   core/lifecycle
   config/schema
   config/loader
   config/defaults
   contracts/models
   contracts/protocols
   contracts/errors
   connectors/index
   plugins/index
   utils/index
   cli/index

Entry Points
------------

The core package registers several entry points:

* ``accuralai_core.backends``: Backend implementations
* ``accuralai_core.validators``: Validation plugins  
* ``accuralai_core.caches``: Caching implementations

Configuration
-------------

See the `configuration example <../../plan/accuralai-core-config-example.toml>`_ for setup details.

CLI Usage
---------

.. code-block:: bash

   # Generate text using the CLI
   accuralai generate "Hello, world!"

   # With metadata
   accuralai generate "Hello, world!" --metadata user=developer --metadata session=test

   # With parameters
   accuralai generate "Hello, world!" --param temperature=0.7 --param max_tokens=100

Development
-----------

.. code-block:: bash

   # Install in development mode
   pip install -e packages/accuralai-core[dev]

   # Run tests
   pytest packages/accuralai-core/tests/

   # Run linting
   ruff check packages/accuralai-core/
