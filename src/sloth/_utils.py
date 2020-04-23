# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

__all__ = [
    'check_type', 'is_iterable', 'check_subclass'
]


def check_type(_type, **kwargs):
    for key, val in kwargs.items():
        if not isinstance(val, _type):
            raise TypeError('{} must be {}'.format(key, getattr(_type, '_type_str', _type)))
        

def check_subclass(klass, **kwargs):
    for key, val in kwargs.items():
        if not issubclass(val, klass):
            raise TypeError('{} must be {}'.format(key, getattr(klass, '_type_str', klass)))
        

def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False
