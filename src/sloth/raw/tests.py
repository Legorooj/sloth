# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------
from .._utils import check_type
from .base import Test
from ..timers import Stopwatch
from typing import Mapping

__all__ = [
    'TestCallable', 'TestCallableWithArgs', 'TestEval', 'TestExec'
]


class TestCallable(Test):
    
    def __init__(self, _callable):
        if not callable(_callable):
            raise TypeError('_callable must be a function or be callable')
        self._func = _callable
    
    def run(self):
        s = Stopwatch(start=True)
        self._func()
        return s.stop()


class TestCallableWithArgs(TestCallable):
    
    def __init__(self, _callable, *args, **kwargs):
        super(TestCallableWithArgs, self).__init__(_callable=_callable)
        self._args = args
        self._kwargs = kwargs
    
    def run(self, *args, **kwargs):
        args = args or self._args
        kwargs = kwargs or self._kwargs
        s = Stopwatch(start=True)
        self._func(*args, **kwargs)
        return s.stop()


class TestEval(Test):
    
    def __init__(self, statement, gbls=None, lcls=None):
        self._check_eval_safe(statement)
        self._gbls = gbls or dict()
        self._lcls = lcls or dict()
        check_type(dict, globals=self._gbls)
        check_type(Mapping, locals=self._lcls)
        self._statement = statement
        self._caller = eval
    
    def run(self, gbls=None, lcls=None):
        gbls = gbls or self._gbls
        lcls = lcls or self._lcls
        check_type(dict, globals=gbls)
        check_type(Mapping, locals=lcls)
        s = Stopwatch(start=True)
        self._caller(self._statement, gbls, lcls)
        return s.stop()


class TestExec(TestEval):
    
    def __init__(self, statement, gbls=None, lcls=None):
        super(TestExec, self).__init__(statement, gbls, lcls)
        self._caller = exec
