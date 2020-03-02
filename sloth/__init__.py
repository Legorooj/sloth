# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

__all__ = [
    '__author__', '__author__', '__maintainer__', '__license__', '__uri__', '__version__', 'CompareSloth'
]

__author__ = 'Legorooj'
__maintainer__ = 'Legorooj, FluffyKoalas'

__license__ = 'MIT'

__uri__ = 'https://github.com/FluffyKoalas/sloth'

__version__ = '0.1.dev0'


class CompareSloth:
    
    def __or__(self, other):
        return str(self)
    
    def __str__(self):
        return 'sloth is far better'
