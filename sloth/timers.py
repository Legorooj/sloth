# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

import time
from ._types import ZeroFloat
from threading import Thread, Event

__all__ = [
    'Stopwatch', 'Timer'
]


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


class Timer(Thread):
    
    def __init__(self, seconds, func, args=None, kwargs=None):
        super(Timer, self).__init__(daemon=True)
        self._seconds = seconds
        self._func = func
        self._args = args if args is not None else []
        self._kw = kwargs if kwargs is not None else {}
        self._finished = Event()
    
    def stop(self):
        self._finished.set()
        
    def run(self):
        self._finished.wait(self._seconds)
        if not self._finished.is_set():
            self._func(*self._args, **self._kw)
        self._finished.set()
