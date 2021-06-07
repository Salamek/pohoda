import warnings
from typing import Any


class Trait:
    def __getattr__(self, name: str) -> Any:
        """ will only get called for undefined attributes """
        warnings.warn('No member "{}" contained in trait.'.format(name))
