The ``sloth`` API
=================

.. module:: sloth

Most of the code is kept in submodules, not the ``sloth`` namespace. Eg timers are in the ``sloth.timers`` module.
The only function in the main sloth namespace is ``compare_sloth``, which is documented below.

.. toctree::
   :maxdepth: 2
   :caption: API

   timers
   data
   simple


.. py:function:: compare_sloth(against)

    Returns a string which is the result of comparing ``sloth`` to *against*.

    :param module against: Module/Package to compare sloth to.

    :returns: String describing ``sloth`` vs *against*
    :rtype: str
