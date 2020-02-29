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
    'BYTE', 'KILOBYTE', 'MEGABYTE', 'GIGABYTE', 'TestDataProcessing'
]


BYTE = '#'
KILOBYTE = BYTE * 1024
MEGABYTE = KILOBYTE * 1024
GIGABYTE = MEGABYTE * 1024


class TestDataProcessing:
    """
    TestDataProcessing is a class that runs data
    through a function while timing it.
    """
    
    def __init__(self, func):
        self.func = func
        if not callable(func):
            raise TypeError('Uncallable function')
    
    def run(self, against=None, data=KILOBYTE, average=False, atimes=2):
        if against is None:
            against = [1]
        else:
            check_type(list, against=against)
            
        if not isinstance(data, (str, bytes)):
            raise TypeError('data must be str or bytes')
        
        check_type(bool, average=average)
        check_type(int, atimes=atimes)
        
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
    
    def run_with_progressbar(self, against=None, data=KILOBYTE, average=False, atimes=2):
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
    
        self.func(data*n)
        
        return s.stop()
