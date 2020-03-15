# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------
import pytest
# noinspection PyProtectedMember
from sloth import _utils


def test_check_type():
    _utils.check_type(str, value='A string value')
    _utils.check_type((str, bytes, int), value1='Another string', value2=b'A byte string', value3=1234567890)
    
    with pytest.raises(TypeError):
        _utils.check_type(str, val=b'Not a string')
    
    with pytest.raises(TypeError):
        _utils.check_type((str, int, complex, bytes), val=['a', 'list'])


def test_is_iterable():
    for item in [tuple(), list(), set(), dict()]:
        assert _utils.is_iterable(item)
    
    for item in [int(), complex(), pytest]:
        assert not _utils.is_iterable(item)


def test_is_subclass():
    with pytest.raises(TypeError):
        _utils.check_subclass(int, list=list)
    _utils.check_subclass(int, bool=bool)
