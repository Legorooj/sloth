# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

from threading import Thread, Event

import time

from ._types import ZeroFloat
from ._utils import check_type

__all__ = [
    'Stopwatch', 'Timer'
]


class Stopwatch:
    """
    Simple stopwatch for capturing code execution time.
    """
    
    def __init__(self, start=False):
        self._time = 0
        if start:
            self.start()
    
    def start(self):
        """
        
        Starts the *StopWatch*.
        """
        self._time = time.perf_counter()
    
    def stop(self):
        """
        Clears the stopwatch and returns the time elapsed since the :py:meth:`start` method has been called.
        This method will return ``0`` if start has not been called.

        :returns: The time - in seconds - elapsed since :py:meth:`start` was called
        :rtype: float
        """
        t = ZeroFloat(time.perf_counter()) - self._time
        self._time = 0
        return t
    
    def lap(self):
        """
        Returns the time elapsed since the :py:meth:`start` method was called *without* clearing the stopwatch.
        This method will return ``0`` if start has not been called.

        :returns: The time - in seconds - elapsed since :py:meth:`start` was called
        :rtype: int
        """
        return ZeroFloat(time.perf_counter()) - self._time
    
    @property
    def running(self):
        return self._time != 0
    
    @running.setter
    def running(self, value):
        raise NotImplementedError()


class Timer(Thread):
    """
    Simple timer that executes a function after a timed interval
    """
    
    def __init__(self, seconds, func, args=None, kwargs=None):
        """
        :param int seconds: The number of seconds to call *func* after.
        :param function func: The function to call after *seconds* seconds have elapsed.
        :param args: Positional arguments to pass to *func*.
        :type args: list or tuple or None
        :param kwargs: Keyword arguments to pass to func.
        :type kwargs: dict or None
    
        :raises TypeError: if any of the arguments have incorrect types
        """
        kwargs = kwargs or dict()
        args = args or list()
        
        check_type(int, seconds=seconds)
        if not callable(func):
            raise TypeError('func must be callable')
        check_type((list, tuple), args=args)
        check_type(dict, kwargs=kwargs)
        
        super(Timer, self).__init__(daemon=True)
        self._seconds = seconds
        self._func = func
        self._args = args if args is not None else []
        self._kw = kwargs if kwargs is not None else {}
        self._finished = Event()
    
    def stop(self):
        """
        Cancels the timer. If this method is called before start, then the timer *will not be run*.
        """
        self._finished.set()
    
    def run(self):
        """
        Run the timer in the main thread. This is the same as calling start followed immediately by join.
        """
        self._finished.wait(self._seconds)
        if not self._finished.is_set():
            self._func(*self._args, **self._kw)
        self._finished.set()
