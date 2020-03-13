``sloth.raw.complex.base``: The abstract base classes for testing
=================================================================

.. module:: sloth.raw.complex.base

This module provides the abstract base classes for tests. They are abstract classes, and *must* be subclassed.

.. py:class:: Test(metaclass=abc.ABCMeta)

   This is the base class for *Tests*. That also includes :func:`sloth.runners.AverageRunner`, though that may be
   more accurately classed as a test *runner*, not a test.

   .. py:method:: run()
      :abstractmethod:

      This method is abstract, to be overridden on subclasses. This is the method called by the test runners to run the
      test.
