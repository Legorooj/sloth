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
