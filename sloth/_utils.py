# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------


def check_type(_type, **kwargs):
    for key, val in kwargs.items():
        if not isinstance(val, _type):
            raise TypeError(f'{key} must be {_type}')
