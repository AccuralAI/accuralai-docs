AccuralAI Validator
===================

Validation plugins for AccuralAI LLM pipeline.

Overview
--------

``accuralai-validator`` provides content validation plugins to ensure response quality and safety.

Available Validators
---------------------

* **JSON Validator**: Validates JSON structure and schema
* **Length Validator**: Validates response length constraints
* **Regex Validator**: Validates against regular expressions
* **Toxicity Validator**: Detects toxic or harmful content
* **Prompt Injection Validator**: Detects prompt injection attempts

API Reference
-------------

.. toctree::
   :maxdepth: 2

   base
   config
   exceptions
   telemetry
   validators/index

Usage Examples
--------------

JSON Validator
~~~~~~~~~~~~~~

.. code-block:: python

   from accuralai_validator.validators.json_schema import JSONSchemaValidator

   validator = JSONSchemaValidator(schema={
       "type": "object",
       "properties": {
           "response": {"type": "string"},
           "confidence": {"type": "number"}
       }
   })

   is_valid = await validator.validate({
       "response": "Hello, world!",
       "confidence": 0.95
   })

Length Validator
~~~~~~~~~~~~~~~

.. code-block:: python

   from accuralai_validator.validators.length import LengthValidator

   validator = LengthValidator(
       min_length=10,
       max_length=1000
   )

   is_valid = await validator.validate("This is a valid response.")

Toxicity Validator
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from accuralai_validator.validators.toxicity import ToxicityValidator

   validator = ToxicityValidator(threshold=0.8)
   is_valid = await validator.validate("This is a safe response.")

Configuration
-------------

Validators are registered as entry points under ``accuralai_core.validators``.

Development
-----------

.. code-block:: bash

   # Install in development mode
   pip install -e packages/accuralai-validator[dev]

   # Run tests
   pytest packages/accuralai-validator/tests/
