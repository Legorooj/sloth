``sloth.timers``: Timing functions and classes
==============================================

.. module:: sloth.timers
.. default-domain:: py

The ``sloth.timers`` module contains functions and classes for timing code.

.. py:class:: StopWatch()

    Simple stopwatch for capturing code execution time.

    .. py:method:: start()

        Starts the *StopWatch*.

    .. py:method:: stop()

        Clears the stopwatch and returns the time elapsed since the :py:meth:`start` method has been called.
        This method will return ``0`` if start has not been called.

        :returns: The time - in seconds - elapsed since :py:meth:`start` was called
        :rtype: float

    .. py:method:: lap()

        Returns the time elapsed since the :py:meth:`start` method was called *without* clearing the stopwatch.
        This method will return ``0`` if start has not been called.

        :returns: The time - in seconds - elapsed since :py:meth:`start` was called
        :rtype: int


.. py:class:: Timer(seconds, func, args=None, kwargs=None):

    Simple timer that executes a function after a timed interval

    :param int seconds: The number of seconds to call *func* after.
    :param function func: The function to call after *seconds* seconds have elapsed.
    :param args: Positional arguments to pass to *func*.
    :type args: list or tuple or None
    :param kwargs: Keyword arguments to pass to func.
    :type kwargs: dict or None

    :raises TypeError: if any of the arguments have incorrect types

    .. py:method:: start()

        Start the timer in the background. Eg:

        .. code-block:: python

            >>> from sloth.timers import Timer
            >>> from time import sleep
            >>> def f():
            ...     print('Timer finished')
            ...
            >>> def a():
            ...     t = Timer(5, f)
            ...     t.start()
            ...     print('Doing stuff')
            ...     sleep(3)
            ...     print('Doing more stuff')
            ...     sleep(4)
            ...     print('Finished doing stuff while the timer has executed in the background')
            ...
            >>> a()
            Doing stuff
            Doing more stuff
            Timer
            Finished doing stuff while the timer has executed in the background


    .. py:method:: stop()

        Cancels the timer. If this method is called *before* :py:meth:`start`, then the timer *will not be run*.

    .. py:method:: join(timeout=None)

        Wait until the timer finishes or *timeout*, if not ``None``, has elapsed.

        :param timeout: number of seconds to wait before returning. If None, then it returns when the timer has
                        finished.
        :type timeout: int or float or None

    .. py:method:: run()

        Run the timer in the main thread. This is the same as calling :py:meth:`start` followed immediately by
        :py:meth:`join`

    .. py:attribute:: daemon

        .. warning:: Please do not set this attribute unless you know what you are doing.

        Controls whether or not the underlying thread that runs the timer is daemonic. This must be set *before* calling
        :py:meth:`start`. This value defaults to *True*, meaning that the timer will be canceled if the program ends
        before completion.

        :type: bool
        :default: True
