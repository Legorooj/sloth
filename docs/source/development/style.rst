Our styling guide
=================

We adhere to PEP8. Our CI tests code styling via ``flake8``. If your code doesn't adhere to PEP8, then please reformat.

We also insist that you:

* Add an ``__all__`` statement to your file, or edit the existing one to include your function. *ALL* python files must
  have ``__all__`` definitions, even private ones like ``_types`` and ``_utils``.
