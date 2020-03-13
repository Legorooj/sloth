# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------
import pytest
from sloth import timers, simple
from . import my_func, CallableClass


def test_call_after():
    def kill():
        pytest.fail('Timer failed to stop')
    
    t = timers.Timer(5, kill)
    t.start()
    simple.call_after(4, t.stop)


def test_time_callable():
    simple.time_callable(my_func, n=2, sleep=1)
    simple.time_callable(CallableClass(), n=2, sleep=1)


def test_time_eval():
    simple.time_eval('1 + 1 + 2 + 3 + 5 + 8 + 13')


def test_time_exec():
    simple.time_exec('assert True; assert list() is not None')
