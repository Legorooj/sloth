# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

import pytest
import time
import typing
# noinspection PyProtectedMember
from sloth import simple, timers, _utils, _types
from sloth.raw.complex import tests as complex_tests, base as complex_base, runners as complex_runners


# Testing functions and classes
def my_func(*args, **kwargs):
    assert args != kwargs
    if hasattr(kwargs, 'sleep'):
        time.sleep(kwargs.sleep)


class CallableClass:
    def __call__(self, *args, **kwargs):
        my_func(*args, **kwargs
                )
# End


class TestUtils:
    
    def test_check_type(self):
        _utils.check_type(str, value='A string value')
        _utils.check_type((str, bytes, int), value1='Another string', value2=b'A byte string', value3=1234567890)
        
        with pytest.raises(TypeError):
            _utils.check_type(str, val=b'Not a string')
            
        with pytest.raises(TypeError):
            _utils.check_type((str, int, complex, bytes), val=['a', 'list'])
    
    def test_is_iterable(self):
        for item in [tuple(), list(), set(), dict()]:
            assert _utils.is_iterable(item)
            
        for item in [int(), complex(), pytest]:
            assert not _utils.is_iterable(item)
    
    def test_is_subclass(self):
        with pytest.raises(TypeError):
            _utils.check_subclass(int, list=list)
        _utils.check_subclass(int, bool=bool)


class TestTypes:
    
    def test_code_type(self):
        obj = compile('import antigravity', '<string>', 'exec')
        assert isinstance(obj, _types.CodeObjType)
        assert not isinstance('I\'m a string, not a code type!', _types.CodeObjType)
    
    def test_none_type(self):
        assert isinstance(None, _types.NoneType)
        assert not isinstance(lambda: None, _types.NoneType)
    
    def test_zero_float(self):
        assert _types.ZeroFloat(100) - 0 == 0
        assert _types.ZeroFloat(100) - 1 == 99


class TestTimers:
    
    def test_stopwatch(self):
        s = timers.Stopwatch()
        s.start()
        assert s.running is True
        with pytest.raises(NotImplementedError):
            s.running = False
        time.sleep(0.1)
        assert s.lap() != 0.0
        s.stop()
        assert s.running is False
        
    def test_timer(self):
        def kill():
            pytest.fail('Timer failed to stop')
        t1 = timers.Timer(5, kill)
        t2 = timers.Timer(2, t1.stop)
        t1.start()
        t2.start()
        time.sleep(1)
        t2.join()
        t1.join()


# noinspection PyProtectedMember
class TestRawComplexBase:
    
    def test_subclassing(self):
        class MyTest(complex_base.Test):
            def run(self):
                return True
        
        assert MyTest().run()
        assert issubclass(MyTest, complex_base.Test)
    
    def test_abc(self):
        # noinspection PyAbstractClass
        class MyTest(complex_base.Test):
            pass
        
        with pytest.raises(TypeError):
            MyTest()
    
    def test_eval_safe(self):
        class MyTest(complex_base.Test):
            def run(self):
                pass
        with pytest.raises(TypeError):
            MyTest()._check_eval_safe(list())
        MyTest()._check_eval_safe(str())


class TestRawComplexTests:
    
    def test_callable(self):
        test = complex_tests.TestCallable(my_func)
        test.run()
        with pytest.raises(TypeError):
            test = complex_tests.TestCallable('Not a func')
    
    def test_callable_with_args(self):
        test = complex_tests.TestCallableWithArgs(my_func, 1, 2, 3, key='word', arg='ument')
        test.run(1, 2, 3, key='word', arg='ument', extra=b'arg')
    
    def test_eval(self):
        test = complex_tests.TestEval('1 + 1 + 2 + 3 + 5 + 8 + 13')
        test.run()
    
    def test_exec(self):
        test = complex_tests.TestExec('print("Stuff"); assert True; assert not False')
        test.run()
        

class TestRawComplexRunners:
    
    def test_default_runner(self):
        tests = [
            complex_tests.TestCallable(my_func),
            complex_tests.TestExec('print("Working"); assert True'),
            complex_tests.TestCallableWithArgs(my_func, key='value', foo=b'ar'),
            complex_tests.TestEval('1 * 1 * 2 * 3 * 5 * 8 * 13')
        ]
        runner = complex_runners.TestRunner(tests)
        assert isinstance(runner.run(), typing.Generator)
        assert isinstance(list(runner.run()), list)
    
    def test_average(self):
        tests = [
            complex_runners.AverageTest(
                complex_tests.TestCallable(my_func)
            )
        ]
        runner = complex_runners.TestRunner(tests)
        assert isinstance(runner.run(), typing.Generator)
        assert isinstance(list(runner.run()), list)
    
    def test_average_with_runner(self):
        tests = [
            complex_runners.AverageTest(
                complex_tests.TestCallable(my_func)
            ),
            complex_runners.AverageTest(
                complex_tests.TestExec('print("Working"); assert True')
            ),
            complex_runners.AverageTest(
                complex_tests.TestCallableWithArgs(my_func, key='value', foo=b'ar')
            ),
            complex_runners.AverageTest(
                complex_tests.TestEval('1 * 1 * 2 * 3 * 5 * 8 * 13')
            )
        ]
        runner = complex_runners.TestRunner(tests)
        assert isinstance(runner.run(), typing.Generator)
        assert isinstance(list(runner.run()), list)
        

class TestSimple:
    
    def test_call_after(self):
        def kill():
            pytest.fail('Timer failed to stop')
        
        t = timers.Timer(5, kill)
        t.start()
        simple.call_after(4, t.stop)
        
    def test_time_callable(self):
        simple.time_callable(my_func, n=2, sleep=1)
        simple.time_callable(CallableClass(), n=2, sleep=1)
    
    def test_time_eval(self):
        simple.time_eval('1 + 1 + 2 + 3 + 5 + 8 + 13')
    
    def test_time_exec(self):
        simple.time_exec('assert True; assert list() is not None')


class TestMisc:
    
    def test_raw_simple(self):
        with pytest.raises(NotImplementedError):
            from sloth.raw.simple import simple
            simple()
            
    def test_compare(self):
        from sloth import compare_sloth
        import timeit
        assert compare_sloth(timeit) != compare_sloth(pytest)
