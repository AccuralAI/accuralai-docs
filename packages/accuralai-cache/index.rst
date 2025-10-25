AccuralAI Cache
===============

Caching providers for the AccuralAI LLM pipeline.

Overview
--------

``accuralai-cache`` supplies production-ready caches with multiple storage backends:

* **Memory Cache**: Async LRU with TTL, eager expiry, and hit/miss statistics
* **Disk Cache**: SQLite-based storage with size enforcement and prefix invalidation  
* **Layered Cache**: Composes memory + disk tiers and promotes hits for hot keys

Key Features
------------

* **TTL Support**: Time-to-live expiration for all cache entries
* **Capacity Management**: Configurable size limits and eviction policies
* **Statistics**: Hit/miss ratios and performance metrics
* **Async Interface**: Full async/await support for non-blocking operations

API Reference
-------------

.. toctree::
   :maxdepth: 2

   base
   memory
   disk
   layered

Usage Examples
--------------

Memory Cache
~~~~~~~~~~~~

.. code-block:: python

   from accuralai_cache.memory import build_memory_cache

   cache = build_memory_cache(max_size=1000, ttl=3600)
   await cache.set("key", "value")
   value = await cache.get("key")

Disk Cache
~~~~~~~~~~

.. code-block:: python

   from accuralai_cache.disk import build_disk_cache

   cache = build_disk_cache(db_path="cache.db", max_size=10000)
   await cache.set("key", "value")
   value = await cache.get("key")

Layered Cache
~~~~~~~~~~~~~

.. code-block:: python

   from accuralai_cache.layered import build_layered_cache

   cache = build_layered_cache(
       memory_size=1000,
       disk_path="cache.db",
       disk_size=10000
   )
   await cache.set("key", "value")
   value = await cache.get("key")

Configuration
-------------

Cache implementations are registered as entry points under ``accuralai_core.caches``:

* ``memory``: Memory-based LRU cache
* ``disk``: SQLite-based disk cache
* ``layered``: Combined memory and disk cache

Development
-----------

.. code-block:: bash

   # Install in development mode
   pip install -e packages/accuralai-cache[dev]

   # Run tests
   pytest packages/accuralai-cache/tests/
