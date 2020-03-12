Running and adding to the tests
===============================

* Our tests are kept in the ``tests`` directory, and use ``pytest``. We aim for 101% coverage.

* You can install the testing requirements with ``pip install -r tests/test-requirements.txt``.

* The tests can be run with:

.. code-block:: shell

    pytest --cov=. tests

* If you're not getting 100% coverage, see why with ``coverage html`` and open the html files (under ``htmlcov``) in
  your browser to see which lines aren't being tested. The config is stored in ``.coveragerc``.

* ``flake8`` style testing can be run with just ``flake8 sloth`` to check the directory. The config is stored in
  ``.flake8``.
