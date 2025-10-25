AccuralAI Router
================

Routing strategies for AccuralAI LLM pipeline.

Overview
--------

``accuralai-router`` provides intelligent routing strategies to direct requests to appropriate backends based on various criteria.

Available Strategies
---------------------

* **Direct Router**: Routes to a single specified backend
* **Weighted Router**: Routes based on configurable weights
* **Failover Router**: Routes with fallback options
* **Rules Router**: Routes based on configurable rules
* **Complexity Router**: Routes based on prompt complexity analysis

API Reference
-------------

.. toctree::
   :maxdepth: 2

   base
   config
   strategies/index

Usage Examples
--------------

Direct Router
~~~~~~~~~~~~~

.. code-block:: python

   from accuralai_router.strategies.direct import DirectRouter

   router = DirectRouter(backend_id="ollama")
   backend_id = await router.route({
       "prompt": "Hello, world!",
       "metadata": {"user": "developer"}
   })

Weighted Router
~~~~~~~~~~~~~~~

.. code-block:: python

   from accuralai_router.strategies.weighted import WeightedRouter

   router = WeightedRouter({
       "ollama": 0.7,
       "google": 0.3
   })
   backend_id = await router.route({
       "prompt": "Hello, world!",
       "metadata": {"user": "developer"}
   })

Rules Router
~~~~~~~~~~~

.. code-block:: python

   from accuralai_router.strategies.rules import RulesRouter

   router = RulesRouter({
       "if metadata.user == 'admin': return 'google'",
       "if len(prompt) > 1000: return 'ollama'",
       "default: return 'google'"
   })
   backend_id = await router.route({
       "prompt": "Hello, world!",
       "metadata": {"user": "admin"}
   })

Configuration
-------------

Routers are registered as entry points under ``accuralai_core.routers``.

Development
-----------

.. code-block:: bash

   # Install in development mode
   pip install -e packages/accuralai-router[dev]

   # Run tests
   pytest packages/accuralai-router/tests/
