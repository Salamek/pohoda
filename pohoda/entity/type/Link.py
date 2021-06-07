# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class Link(Agenda):
    _ref_elements = ['sourceDocument', 'settingsSourceDocument']
    _elements = ['sourceAgenda', 'sourceDocument', 'settingsSourceDocument']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('link', 'typ')
        self._add_elements(xml, self._elements, 'typ')
        return xml
