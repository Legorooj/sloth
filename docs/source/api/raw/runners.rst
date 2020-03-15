``sloth.raw.runners``: Multiple test runners
====================================================

.. module:: sloth.raw.runners
.. default-domain:: py

This module provides utilities for running multiple tests, or averaging tests.


.. py:class:: TestRunner(tests)

   Convenience class to run multiple tests.

   :param tests: List of :py:class:`sloth.raw.base.Test` instances to run
   :type tests: list or tuple or set

   .. py:method:: run()

      Generator, returns the results of running each test.

      :rtype: generator
      :returns: Time it took to run each tests.


.. py:class:: AverageTest(test, n=None)

   Run test *n* times and return the average time it took to run it.

   :param Test test: Test to average
   :param int n: Number of times to run the test - the higher the more accurate. Defaults to 2.

   .. py:method:: run(n=None)

      Run the average test, and return how long it took to run it, averaged.

      :param int n: Use this to override the *n* parameter passed in upon creation.
      :returns: How long it took to run the test, averaged
      :rtype: float
