The raw ``sloth`` API
=====================

The ``sloth.raw`` module contains all of the classes and functions that do the grunt work for the user, allowing the
smallest amount of code required on the users end. All of the classes and functions are aiming to be as clean and
efficient as possible, so if you come across something that can be optimized, let us know!

This module is split into two parts; ``sloth.raw.simple`` and ``sloth.raw.complex``. In the former you'll find mostly
functions for single call and simpler testing. The latter is where you'll find the more complex base API.

.. toctree::
   :maxdepth: 2
   :caption: The sloth.raw API reference

   simple
   complex/index
