# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------
import typing
from sloth.raw import runners, tests
from . import my_func, CallableClass


def test_default_runner():
    test_list = [
        tests.TestCallable(my_func),
        tests.TestExec('print("Working"); assert True'),
        tests.TestCallableWithArgs(my_func, key='value', foo=b'ar'),
        tests.TestEval('1 * 1 * 2 * 3 * 5 * 8 * 13')
    ]
    runner = runners.TestRunner(test_list)
    assert isinstance(runner.run(), typing.Generator)
    assert isinstance(list(runner.run()), list)


def test_average():
    test_list = [
        runners.AverageTest(
            tests.TestCallable(my_func)
        )
    ]
    runner = runners.TestRunner(test_list)
    assert isinstance(runner.run(), typing.Generator)
    assert isinstance(list(runner.run()), list)


def test_average_with_runner():
    test_list = [
        runners.AverageTest(
            tests.TestCallable(my_func)
        ),
        runners.AverageTest(
            tests.TestExec('print("Working"); assert True')
        ),
        runners.AverageTest(
            tests.TestCallableWithArgs(my_func, key='value', foo=b'ar')
        ),
        runners.AverageTest(
            tests.TestEval('1 * 1 * 2 * 3 * 5 * 8 * 13')
        )
    ]
    runner = runners.TestRunner(test_list)
    assert isinstance(runner.run(), typing.Generator)
    assert isinstance(list(runner.run()), list)
