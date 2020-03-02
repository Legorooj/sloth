Development
===========

Seeing as ``sloth`` is an open source project, contributions are welcome! This allows us to provide features that the
community want to be included.

If you've found a bug, or would like to request a feature, please submit it on our
`issue tracker <https://github.com/fluffykoalas/issues>`_ on GitHub.

Quickstart
----------

1 Our repository is at `<https://github.com/fluffykoalas/sloth>`_.

  * Development is done on the ``dev`` branch. Pull Requests should be filed against this branch, not the master branch.
  * Stable releases reside on the ``master`` branch.

2. Fork the repository into your own account.

3. Create a new branch for you patch/feature

4. Commit as often as you'd like, but:

  * Make sure the commits are logical and precise *before* asking for code review. Please see the
     :doc:`commit-guideline` section for more info.
  * Adhere to PEP8 - if your code doesn't adhere, it won't be merged.
  * If applicable, provide tests for your code. We aim to have around 99% code coverage in testing.

5. Add a changelog entry - see :doc:`changelog-guide` for details.

6. For new files, add the copyright header. It can be found in the ``sloth.__init__`` file.

7. Squish, squash, rebase and revert commits as asked by reviewers.




.. toctree::
   :maxdepth: 2
   :caption: Development

   changelog-guide
   commit-guideline
