# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

# noinspection PyProtectedMember
from sloth import _types


def test_code_type():
    obj = compile('import antigravity', '<string>', 'exec')
    assert isinstance(obj, _types.CodeObjType)
    assert not isinstance('I\'m a string, not a code type!', _types.CodeObjType)


def test_none_type():
    assert isinstance(None, _types.NoneType)
    assert not isinstance(lambda: None, _types.NoneType)


def test_zero_float():
    assert _types.ZeroFloat(100) - 0 == 0
    assert _types.ZeroFloat(100) - 1 == 99
