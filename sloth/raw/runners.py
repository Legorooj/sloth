# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------
from .._utils import check_type, check_subclass
from .base import Test

__all__ = [
    'TestRunner', 'AverageTest'
]


class TestRunner:
    
    def __init__(self, tests):
        check_type((list, tuple, set), tests=tests)
        for test in tests:
            check_subclass(Test, test=test.__class__)
        self._tests = tests
    
    def run(self):
        for test in self._tests:
            yield test.run()


class AverageTest(Test):
    
    def __init__(self, test, n=None):
        self._n = n
        if self._n is None:
            self._n = 2
        check_type(int, n=self._n)
        check_subclass(Test, test=test.__class__)
        self._test = test
    
    def run(self, n=None):
        n = n or self._n
        check_type(int, n=n)
        return sum([self._test.run() for _ in range(n)]) / n
