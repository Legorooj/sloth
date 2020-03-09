# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

from sloth.timers import Timer, Stopwatch
from sloth._utils import check_type

__all__ = [
    'call_after', 'time_func', 'time_code'
]


def call_after(seconds, func, args=None, kwargs=None):
    Timer(seconds, func, args, kwargs).start()
    
    
def time_func(func, iterations=1000):
    check_type(int, iterations=iterations)
    times = []
    for i in range(iterations):
        s = Stopwatch()
        s.start()
        func()
        times.append(s.stop())
    return sum(times) / len(times)


def time_code(snippet, iterations=1000, gs=None, lcs=None):
    check_type(int, iterations=iterations)
    check_type(str, snippet=snippet)
    times = []
    for i in range(iterations):
        s = Stopwatch()
        s.start()
        eval(snippet, gs or {}, lcs or {})
        times.append(s.stop())
    return sum(times) / len(times)
