# coding: utf-8

from pohoda.entity.common.Trait import Trait


class SetNodeNameTrait(Trait):
    _node_name = None

    def set_node_name(self, node_name: str) -> None:
        self._node_name = node_name
