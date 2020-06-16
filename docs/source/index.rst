``sloth/docs``
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

See? described in 3 lines. *Everything* that ``timeit`` can do, ``sloth`` can do better. And *most* (speedtest-related)
things ``timeit`` *can't* do ``sloth`` can do anyway.

Or, for the bash ninjas and command liners:

.. code-block::

    $ sloth compare timeit
    sloth is loads better than timeit!
    $ python3 -m sloth compare timeit
    sloth is loads better than timeit!

A Quick Example
---------------

.. code-block:: python

    >>> from sloth.simple import time_callable
    >>> import time
    >>> def my_func(a, b, c):
    ...     time.sleep(1)
    ...     print(a, b, c)
    >>> time_callable(my_func, 2, 'a', 'b', 'c')
    a b c
    a b c
    1.0150199500000028

Installation
------------

You can install sloth with pip:

.. code-block:: shell

    pip install sloth-speedtest

Please see :doc:`installation` for more information.


Usage
-----

Please see the :doc:`api/index` for API usage guidance. Please run ``sloth -h`` or ``sloth --help`` for help with the
command line tool.


Links
-----

* `PyPI <https://pypi.org/project/sloth-speedtest>`_
* `GitHub <https://github.com/fluffykoalas/sloth>`_
* `Docs <https://sloth.fluffykoalas.org/en/stable>`_


Index
-----

.. toctree::
   :maxdepth: 2
   :caption: API reference

   api/index


.. toctree::
   :maxdepth: 2
   :caption: The sloth project

   installation
   changelog
   development/index


Indices and Tables
------------------

* :ref:`genindex`
