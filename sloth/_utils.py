# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

__all__ = [
    'check_type', 'is_iterable', 'is_function_or_callable'
]


def check_type(_type, **kwargs):
    for key, val in kwargs.items():
        if not isinstance(val, _type):
            raise TypeError('{} must be {}'.format(key, _type))
        

def is_iterable(f):
    if hasattr(f, '__iter__'):
        return True
    return False


def is_function_or_callable(f):
    if hasattr(f, '__call__') or callable(f):
        return True
    if isinstance(f, type(type)):
        return True
    return False
