# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

from .timers import Timer
from .raw import tests, runners

__all__ = [
    'call_after', 'time_callable', 'time_eval', 'time_exec'
]


def call_after(seconds, func, args=None, kwargs=None):
    Timer(seconds, func, args, kwargs).start()


def time_callable(func, n=2, *args, **kwargs):
    test = tests.TestCallableWithArgs(func, *args, **kwargs)
    runner = runners.AverageTest(test, n)
    return runner.run()


def time_eval(snippet, n=2, gbls=None, lcls=None):
    test = tests.TestEval(snippet, gbls, lcls)
    runner = runners.AverageTest(test, n)
    return runner.run()


def time_exec(snippet, n=2, gbls=None, lcls=None):
    test = tests.TestExec(snippet, gbls, lcls)
    runner = runners.AverageTest(test, n)
    return runner.run()
