# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------
import pytest
from sloth.raw import tests
from . import my_func


def test_callable():
    test = tests.TestCallable(my_func)
    test.run()
    with pytest.raises(TypeError):
        tests.TestCallable('Not a func')


def test_callable_with_args():
    test = tests.TestCallableWithArgs(my_func, 1, 2, 3, key='word', arg='ument')
    test.run(1, 2, 3, key='word', arg='ument', extra=b'arg')


def test_eval():
    test = tests.TestEval('1 + 1 + 2 + 3 + 5 + 8 + 13')
    test.run()


def test_exec():
    test = tests.TestExec('print("Stuff"); assert True; assert not False')
    test.run()
