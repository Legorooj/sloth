# ----------------------------------------------------------------------------
# Copyright (c) 2020 Legorooj <legorooj@protonmail.com>
# Copyright (c) 2020 FluffyKoalas <github.com/fluffykoalas>
# This file and all others in this project are licensed under the MIT license.
# Please see the LICENSE file in the root of this repository for more details.
# ----------------------------------------------------------------------------

"""
sloth.raw.complex.base provides the abstract base classes for the sloth.raw module.
"""

import abc
from .._types import CodeObjType

__all__ = ['Test']


class Test(metaclass=abc.ABCMeta):
    """
    Abstract base class for tests
    """
    
    @property
    def _type_str(self):
        return 'Test or subclass'
    
    @abc.abstractmethod
    def run(self):
        pass
    
    @staticmethod
    def _check_eval_safe(obj):
        if not isinstance(obj, (CodeObjType, str, bytes)):
            raise TypeError('obj must be a compiled code object, string, or bytes-like-object')
        if not isinstance(obj, CodeObjType):
            try:
                compile(obj, '<string>', 'exec')
            except Exception:
                raise ValueError('unable to compile code snippet')
