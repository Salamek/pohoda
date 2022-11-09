from typing import List
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.SetNamespaceTrait import SetNamespaceTrait


class Part(Agenda, SetNamespaceTrait):
    _node_prefix = None

    _elements = []  # type: List[str]

    def set_node_prefix(self, prefix: str) -> None:
        self._node_prefix = prefix

    def get_xml(self) -> etree.Element:
        raise NotImplementedError
