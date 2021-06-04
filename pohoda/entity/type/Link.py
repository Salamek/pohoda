# coding: utf-8

from pohoda.entity.Agenda import Agenda


class Link(Agenda):
    _ref_elements = ['sourceDocument', 'settingsSourceDocument']
    _elements = ['sourceAgenda', 'sourceDocument', 'settingsSourceDocument']

    def get_xml(self):
        xml = self._create_xml_tag('link', 'typ')
        self._add_elements(xml, self._elements, 'typ')
        return xml
