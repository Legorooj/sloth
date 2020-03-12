``sloth.raw.complex.tests``: Standard tests classes
===================================================

.. module:: sloth.raw.complex.tests
.. default-domain:: py


.. py:class:: TestCallable(_callable)

   This test tests a callable object; any object that ``callable(obj)`` is ``True``.

   :param callable _callable: The callable object to speedtest

   .. py:method:: run()

      Speedtest the callable and return how long it took to execute.

      :return: How long the callable took to run
      :rtype: float


.. py:class:: TestCallableWithArgs(_callable, *args, **kwargs)

   This test is similar to :class:`TestCallable`, but the callable has args when using this test.

   :param callable _callable: The callable object to speedtest
   :param args: Arguments to pass to the callable object.
   :param kwargs: Keyword arguments to pass to the callable object.

   .. code-block:: python

      >>> from sloth.raw.complex.tests import TestCallableWithArgs
      >>> def my_func(a, b, c, d='foo', e='bar'):
      ...     print(a, b, c, d, e)
      >>> my_test = TestCallableWithArgs(my_func, 1, 2, 3, 'bar', 'foo')
      >>> my_test.run()
      1 2 3 bar foo
      0.0
      >>>

   .. py:method:: run(*args, **kwargs)

      Speedtest the callable and return how long it took to execute. ``args`` and ``kwargs`` can be used to override
      those passed in at creation.

      :return: How long the callable took to run
      :rtype: float


.. py:class:: TestEval(statement, gbls=None, lcls=None)

   Speedtest ``eval(statement, gbls, lcls)``. See the
   `eval docs <https://docs.python.org/3/library/functions.html#eval>`_ docs for more info.

   :param statement: The code statement to evaluate.
   :type statement: str or bytes or code

   .. py:method:: run(gbls=None, lcls=None)

      Evaluate the statement, and return how long it took to execute. See the
      `eval docs <https://docs.python.org/3/library/functions.html#eval>`_ docs for more info.

      :return: How long the evaluation took to run
      :rtype: float


.. py:class:: TestExec(statement, gbls=None, lcls=None)

   Speedtest ``exec(statement, gbls, lcls)``. See the
   `exec docs <https://docs.python.org/3/library/functions.html#exec>`_ for more info.

   :param statement: The code statement to execute.
   :type statement: str or bytes or code

   .. py:method:: run(gbls=None, lcls=None)

      Execute the statement, and return how long it took to execute. See the
      `exec docs <https://docs.python.org/3/library/functions.html#exec>`_ for more info.

      :return: How long the evaluation took to run
      :rtype: float
