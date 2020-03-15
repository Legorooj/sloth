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


.. py:function:: time_callable(callable, n, *args, **kwargs)

    Time how long it takes to execute *_callable*, run *iterations* times and averaged.

    :param function func: The callable object to time
    :param int n: Number of times to run and average *_callable*
    :param args: Positional arguments to be passed directly to *_callable*
    :param kwargs: Keyword arguments to be passed directly to *_callable*

    :returns: how long it took for the callable to run, averaged
    :rtype: float

    :raises TypeError: if any of the arguments have incorrect types


.. py:function:: time_eval(snippet, n, gbls=None, lcls=None)

   Speedtest ``eval(statement, gbls, lcls)``. See the
   `eval docs <https://docs.python.org/3/library/functions.html#eval>`_ docs for more info.

   :param snippet: The code statement to evaluate.
   :type snippet: str or bytes or code
   :param int n: Number of times to run and average the code.

   :return: How long the evaluation took to run
   :rtype: float


.. py:function:: time_exec(snippet, n, gbls=None, lcls=None)

   Speedtest ``exec(statement, gbls, lcls)``. See the
   `exec docs <https://docs.python.org/3/library/functions.html#exec>`_ docs for more info.

   :param snippet: The code statement to execute.
   :type snippet: str or bytes or code
   :param int n: Number of times to run and average the code.

   :return: How long the execute took to run
   :rtype: float
