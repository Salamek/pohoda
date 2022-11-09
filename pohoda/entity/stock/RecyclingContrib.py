# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda


class RecyclingContrib(Agenda):
    _elements = ['recyclingContribType', 'coefficientOfRecyclingContrib']
    _ref_elements = ['recyclingContribType']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('recyclingContrib', namespace='stk')
        self._add_elements(xml, self._elements, 'stk')
        return xml
