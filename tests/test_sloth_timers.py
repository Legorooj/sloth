# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

import pytest
import time
from sloth.timers import Stopwatch, Timer


def test_stopwatch():
    s = Stopwatch()
    s.start()
    assert s.running is True
    with pytest.raises(NotImplementedError):
        s.running = False
    time.sleep(0.1)
    assert s.lap() != 0.0
    s.stop()
    assert s.running is False


def test_timer():
    def kill():
        pytest.fail('Timer failed to stop')
    
    t1 = Timer(5, kill)
    t2 = Timer(2, t1.stop)
    t1.start()
    t2.start()
    time.sleep(1)
    t2.join()
    t1.join()
