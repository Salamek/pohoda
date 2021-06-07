# coding: utf-8

from pohoda.entity.common.Trait import Trait


class SetNamespaceTrait(Trait):
    _namespace = None

    def set_namespace(self, namespace: str) -> None:
        self._namespace = namespace
