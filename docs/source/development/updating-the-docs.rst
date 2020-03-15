Updating the documentation
==========================

``sloth``'s documentation is build with `Sphinx <https://sphinx-doc.org>`_. We use Sphinx's default, reStructuredText,
as our markup language.

The documentation is maintained in the main repository, under the ``docs`` folder.

Once you've made your changes, call ``make clean && make html`` to build the docs, then verify that the generated pages
are valid. Please look out for and fix any errors that show up in the build.

To reference commits in the docs, please only have the first 5-7 chars of the commit, and format the link as follows:

.. code-block::

    `cdaf638 <https://github.com/fluffykoalas/sloth/commit/cdaf638>`_

To reference an issue or pull request, please do so like:

.. code-block::

    `Issue #ISSUE-ID <https://github.com/fluffykoalas/sloth/issues/ISSUE-ID>`_
    `Pull Request #PR-ID <https://github.com/fluffykoalas/sloth/pull/PR-ID>`_

