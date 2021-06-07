# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class Filter(Agenda):
    _elements = ['id']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('filter', namespace='ftr')
        self._add_elements(xml, self._elements, 'ftr')
        return xml
