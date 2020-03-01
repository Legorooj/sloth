# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

from sloth.timers import Timer

__all__ = [
    'call_after'
]


def call_after(seconds, func, args=None, kwargs=None):
    Timer(seconds, func, args, kwargs).start()
