Commit guidelines
=================

TL;DR
-----

A commit:

* Stands alone as a single, complete, logical change.
* Has a descriptive commit message
* Has no extraneous modifications - eg fixing a typo in an unrelated file

Avoid committing several unrelated changes in one go.
It makes merging difficult, and also makes it harder to determine which change is the culprit if a bug crops up.

If you did several unrelated changes before committing, ``git gui`` makes committing selected parts and even selected
lines easy. Try the context menu within the window's diff area.

This results in a more readable history, which makes it easier to understand why a change was made - and which changes
caused a bug.


In detail
---------

A commit should be one (and just one) logical unit. If you'd made the following changes:

.. code-block:: python

    @@ -4,11 +4,11 @@
     # This file and all others in this project are licensed under the MIT license.
     # Please see the LICENSE file in the root of this repository for more details.
     # ----------------------------------------------------------------------------

     __all__ = [
    -    '__author__', '__author__', '__maintainer__', '__license__', '__uri__', '__version__', 'CompareSloth'
    +    '__author__', '__author__', '__maintainer__', '__license__', '__uri__', '__version__', 'compare_sloth'
     ]

     __author__ = 'Legorooj'
     __maintainer__ = 'Legorooj, FluffyKoalas'

    @@ -17,12 +17,10 @@ __license__ = 'MIT'
     __uri__ = 'https://github.com/FluffyKoalas/sloth'

     __version__ = '0.1.dev0'


    -class CompareSloth:
    -
    -    def __or__(self, other):
    -        return str(self)
    -
    -    def __str__(self):
    -        return 'sloth is far better'
    +def compare_sloth(against):
    +    if hasattr(against, 'dummy_src_name') and getattr(against, 'dummy_src_name') == '<timeit-src>':
    +        return 'sloth is loads better than timeit!'
    +    else:
    +        return 'sloth is definitely better... assuming that\'s used for timing.'


Then the commit message would be:

.. code-block::

    Replace the CompareSloth class with a function

You can, in fact, view this commit on github: `0d8abc <https://github.com/fluffykoalas/sloth/commit/0d8abc>`_.

Use ``git rebase -i`` to sort, squash, and fix-up commits prior to submitting the pull-request. Make it a readable
history, easy to understand what you’ve done.

Commit messages should provide enough information to enable a third party to decide if the change is relevant to them
and if they need to read the change itself.

Also please set the correct author and email if using ``git`` on the CLI. You can set these like:

    git config --global user.name "Firstname Lastname"
    git config --global user.email "your_email@youremail.com"

Optionally remove the ``--global`` flag to set them for just that repo.
