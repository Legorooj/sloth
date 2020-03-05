``sloth\docs``
==============

*The* python speedtesting library
---------------------------------

``sloth`` is a Python package for speedtesting python code and functions with as little code as necessary.
It's easy to use and, unlike many projects, has decent documentation.

The idea behind this API is:

.. code-block:: python

    >>> from sloth import compare_sloth
    >>> import timeit
    >>> compare_sloth(timeit)
    'sloth is loads better than timeit!'

See? described in 3 lines. *Everything* that ``timeit`` can do, ``sloth`` can do better. And *most* things ``timeit``
*can't* do ``sloth`` can do anyway.


Installation
------------

You can install sloth with pip:

.. code-block:: shell

    pip install sloth-speedtest

Please see :doc:`installation` for more information.


Usage
-----

Please see the :doc:`api/index` or :doc:`examples/index`.


Links
-----

* `PyPI <https://pypi.org/project/sloth-speedtest>`_
* `GitHub <https://github.com/fluffykoalas/sloth>`_


Index
-----

.. toctree::
   :maxdepth: 2
   :caption: API reference

   api/index


.. toctree::
   :maxdepth: 2
   :caption: Examples

   examples/index


.. toctree::
   :maxdepth: 2
   :caption: The sloth project

   installation
   changelog
   development/index

