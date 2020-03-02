# `sloth`

#### *The* python speedtesting library and command line tool

`sloth` is a Python package for speedtesting python code and functions with as little code as necessary.
It's easy to use and, unlike many projects, has decent documentation.

The idea behind this API is:

```python
>>> from sloth import CompareSloth
>>> import timeit
>>> CompareSloth() or timeit
'sloth is far better'
```

See? described in 3 lines. *Everything* that `timeit` can do, `sloth` can do better. And *most* things `timeit` *can't*
do `sloth` can do anyway.

You can also do it from the command line:

```
$ sloth compare timeit
sloth is far better
```
or
```
$ python -m sloth compare timeit
sloth is far better
```


## Installation

You can install sloth with pip:

.. code-block:: shell

    pip install sloth-speedtest

Please see the docs for more info.

## Links

* [PyPI](https://pypi.org/project/sloth-speedtest)
* [Documentation](https://sloth-speedtest.readthedocs.io)
