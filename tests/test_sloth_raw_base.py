# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------
import pytest
from sloth.raw import base


def test_subclassing():
    class MyTest(base.Test):
        def run(self):
            return True
    
    assert MyTest().run()
    assert issubclass(MyTest, base.Test)


def test_abc():
    # noinspection PyAbstractClass
    class MyTest(base.Test):
        pass
    
    with pytest.raises(TypeError):
        MyTest()


# noinspection PyProtectedMember
def test_eval_safe():
    
    with pytest.raises(TypeError):
        base.Test._check_eval_safe(list())
    base.Test._check_eval_safe(str())
