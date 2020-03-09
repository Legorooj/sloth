# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------
from ..timers import Stopwatch
from .._utils import check_type
import tqdm

__all__ = [
    'BYTE', 'KILOBYTE', 'MEGABYTE', 'GIGABYTE', 'TestIncrementalDataProcessing'
]

BYTE = '#'
KILOBYTE = BYTE * 1024
MEGABYTE = KILOBYTE * 1024
GIGABYTE = MEGABYTE * 1024


class TestRunner:
    
    def __init__(self, tests):
        check_type(list, tests=tests)
        for i in range(len(tests)):
            check_type(Test, **{'test in tests, index {}'.format(i): tests[i]})
        self._tests = tests
        
    def run(self):
        for test in self._tests:
            yield test.run()
        

class Test:
    """
    Base test class for subclassing
    """
    
    @property
    def _type_str(self):
        return 'Test or subclass'
    
    def run(self):
        pass
    

class TestCallable(Test):
    
    def __init__(self, _callable):
        if not callable(_callable):
            raise TypeError('_callable must be a function or be callable')
        self._func = _callable
    
    def run(self):
        s = Stopwatch()
        s.start()
        self._func()
        return s.stop()
    

class TestCallableWithArgs(TestCallable):
    
    def __init__(self, _callable, *args, **kwargs):
        super(TestCallableWithArgs, self).__init__(_callable=_callable)
        self._args = args or ()
        self._kwargs = kwargs or dict()
    
    def run(self, *args, **kwargs):
        s = Stopwatch()
        s.start()
        self._func(*args, **kwargs)
        return s.stop()


class AverageTest(Test):
    
    def __init__(self, test, n=None):
        if n is None:
            self._n = 2
        check_type(int, n=n)
        check_type(Test, test=test)
        self._test = test
    
    def run(self, n=None):
        if n is None:
            n = self._n
        check_type(int, n=n)
        return sum([self._test.run() for _ in range(n)]) / n


class _SuccessiveArgSetTesting:
    """
    Test Sets of args against
    """
    
    def __init__(self, func):
        if not callable(func):
            raise TypeError('func must be callable')
        self._func = func
    
    def run(self, arg_sets):
        return list(self.run_generator(arg_sets))
    
    def run_generator(self, arg_sets, average=False, atimes=2):
        if not isinstance(arg_sets, tuple):
            raise TypeError('arg_sets must be tuple')
        for each_set in arg_sets:
            if average:
                yield sum(map(self._run, [each_set]*atimes)) / atimes
            else:
                yield self._run(each_set)
    
    def _run(self, arg_set):
        s = Stopwatch()
        s.start()
        self._func(*arg_set[0], **arg_set[1])
        return s.stop()


class TestIncrementalDataProcessing:
    """
    TestDataProcessing is a class that runs data
    through a function while timing it.
    """
    
    def __init__(self, func):
        """
        Constructor
        :param func: function to speedtest
        :type func: function
        """
        if not callable(func):
            raise TypeError('func must be callable')
        self._func = func
    
    def run(self, against=None, data=KILOBYTE, average=False, atimes=2, generator=False):
        """
        Run the speedtest

        :param against: list of integers to run against
        :type against: list[int]
        :param data: data to run through the function
        :type data: str
        :param average: average the speedtest to get more accurate results
        :type average: bool
        :param atimes: number of times to average. Defaults to 2.
        :type atimes: int
        :param generator: Run as a generator. This is used for exceptionally large runs.
        :type generator: bool
        :return: list containing the length(s) of time that it took to run the function
        """
        if against is None:
            against = [1]
        else:
            check_type(list, against=against)
        
        if not isinstance(data, (str, bytes)):
            raise TypeError('data must be str or bytes')
        
        check_type(bool, average=average)
        check_type(int, atimes=atimes)
        
        if generator:
            return self._run_generator(against, data, average, atimes)
        
        times = []
        
        for index in range(len(against)):
            if average:
                averagetimes = []
                for i in range(atimes):
                    averagetimes.append(self._run(against[index], data))
                times.append(sum(averagetimes) / len(averagetimes))
            else:
                times.append(self._run(against[index], data))
        
        return times
    
    def _run_generator(self, against, data, average, atimes):
        for index in range(len(against)):
            if average:
                averagetimes = []
                for i in range(atimes):
                    averagetimes.append(self._run(against[index], data))
                yield sum(averagetimes) / len(averagetimes)
            else:
                yield self._run(against[index], data)
    
    def run_with_progressbar(self, against=None, data=KILOBYTE, average=False, atimes=2):
        """
        Run the speedtest with a command line progress bar

        :param against: list of integers to run against
        :type against: list[int]
        :param data: data to run through the function
        :type data: str
        :param average: average the speedtest to get more accurate results
        :type average: bool
        :param atimes: number of times to average. Defaults to 2.
        :type atimes: int
        :return: list containing the length(s) of time that it took to run the function
        """
        
        if against is None:
            against = [1]
        
        times = []
        
        for index in tqdm.tqdm(range(len(against))):
            if average:
                averagetimes = []
                for i in range(atimes):
                    averagetimes.append(self._run(against[index], data))
                times.append(sum(averagetimes) / len(averagetimes))
            else:
                times.append(self._run(against[index], data))
        
        return times
    
    def _run(self, n, data):
        s = Stopwatch()
        s.start()
        
        self._func(data * n)
        
        return s.stop()
