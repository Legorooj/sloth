# `sloth`

#### *The* python speedtesting library and command line tool

`sloth` is a Python package for speedtesting python code and functions with as little code as necessary.
It's easy to use and, unlike many projects, has decent documentation.

The idea behind this API is:

```python
>>> from sloth import compare_sloth
>>> import timeit
>>> compare_sloth(timeit)
'sloth is loads better than timeit!'
```

See? described in 3 lines. *Everything* that `timeit` can do, `sloth` can do better. And *most* things `timeit` *can't*
do `sloth` can do better.

You can also do it from the command line:

```
$ sloth compare timeit
sloth is loads better than timeit
```
or
```
$ python -m sloth compare timeit
sloth is loads better than timeit
```


## Installation

You can install sloth with pip:

```
pip install sloth-speedtest
```

Please see the docs for more info.

## Links

* [PyPI](https://pypi.org/project/sloth-speedtest)
* [Documentation](https://sloth.fluffykoalas.org)


Note that this library is unrelated and mutually exclusive to 
the one at https://sloth.readthedocs.io
