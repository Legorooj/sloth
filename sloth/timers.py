# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

import time
from ._types import ZeroFloat


class Stopwatch:
    """
    Base stopwatch class for timing.
    There may be slight overhead on this class of ~1 microseconds (~0.0001s)
    """
    
    def __init__(self):
        self._time = 0
    
    def start(self):
        self._time = time.time()
    
    def stop(self):
        """
        Get the amount of time since start was called, and reset the timer.
        :return: The amount of time since `start` was called.
        """
        t = ZeroFloat(time.time()) - self._time
        self._time = 0
        return t
    
    def lap(self):
        return ZeroFloat(time.time()) - self._time
