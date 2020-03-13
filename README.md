# `sloth`

#### *The* python speedtesting library and command line tool

[![codecov](https://codecov.io/gh/fluffykoalas/sloth/branch/dev/graph/badge.svg)](https://codecov.io/gh/fluffykoalas/sloth)
[![Build Status](https://dev.azure.com/FluffyKoalas/Sloth/_apis/build/status/fluffykoalas.sloth?branchName=dev)](https://dev.azure.com/FluffyKoalas/Sloth/_build/latest?definitionId=2&branchName=dev)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/3f46b1c00c674ce4b614be082c17ef5b)](https://www.codacy.com/gh/fluffykoalas/sloth?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=fluffykoalas/sloth&amp;utm_campaign=Badge_Grade)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://choosealicense.com/licenses/mit/)

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
