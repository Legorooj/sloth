``sloth.simple``: Simple timing functions
=========================================

.. module:: sloth.simple
.. default-domain:: py

``sloth.simple`` is a module providing helpful functions that are generally simpler to use than the classes
they wrap in the main API.

.. py:function:: call_after(seconds, func, args=None, kwargs=None)

    Call *func* after *seconds* have elapsed.

    :param int seconds: The number of seconds to call *func* after.
    :param function func: The function to call after *seconds* seconds have elapsed.
    :param args: Positional arguments to pass to *func*.
    :type args: list or tuple or None
    :param kwargs: Keyword arguments to pass to func.
    :type kwargs: dict or None

    :raises TypeError: if any of the arguments have incorrect types


.. py:function:: time_func(func, iterations)

    Time how long it takes to execute *func*, run *iterations* times and averaged.

    :param function func: The function to time
    :param int iterations: The number of times to time *func*

    :returns: how long it took for the function to run, averaged
    :rtype: float

    :raises TypeError: if any of the arguments have incorrect types


.. py:function:: time_code(snippet, iterations, gs=None, lcs=None)

    Time how long it takes to ``eval(snippet, gs, lcs)``, run *iterations* times and averaged.

    :param function func: The snippet to time
    :param int iterations: The number of times to time *snippet*
    :param gs: globals to pass to the eval statement. If not specified, the code will run in a clean environment.
    :param lcs: locals to pass to the eval statement. If not specified, the code will run in a clean environment.
    :type gs: dict or None
    :type lcs: dict or None

    :returns: how long it took for the *snippet* to run, averaged
    :rtype: float

    :raises TypeError: if any of the arguments have incorrect types
