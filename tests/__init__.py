# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

"""
Functions/Classes used in multiple tests
"""

import time


def my_func(*args, **kwargs):
    assert args != kwargs
    if hasattr(kwargs, 'sleep'):
        time.sleep(kwargs.sleep)


class CallableClass:
    def __call__(self, *args, **kwargs):
        my_func(*args, **kwargs
                )
