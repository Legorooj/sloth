Our styling guide
=================

We adhere to PEP8, with the exception of the line limit, which we set to 120.
Our CI tests code styling via ``flake8``. If your code doesn't adhere to (our version of) PEP8, then please reformat it.

We also insist that you:

* Add an ``__all__`` statement to your file, or edit the existing one to include your function. *All* python
  modules/submodules must have ``__all__`` definitions, even private modules like ``_types`` and ``_utils``.
