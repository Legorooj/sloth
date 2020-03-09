``sloth.data``: Timed data processing
=====================================

The ``sloth.raw`` module is designed for processing data and argument sets (in large and small amounts) and timing it
with the smallest amount of code required on the users end. All of the classes and functions are highly efficient, and
even allow the user to run matrix style testing jobs, similar to what you'd have in CI.

This module is split into two parts; ``sloth.raw.simple`` and ``sloth.raw.complex``. In the former you'll find mostly
functions for single call and simpler testing. The latter is where you'll find the raw, and more complex, API.

.. toctree::
   :maxdepth: 2
   :caption: The sloth.raw API reference

   simple
   complex/index
