# coding: utf-8

from pohoda.entity.Agenda import Agenda


class Filter(Agenda):
    _elements = ['id']

    def get_xml(self):
        xml = self._create_xml_tag('filter', namespace='ftr')
        self._add_elements(xml, self._elements, 'ftr')
        return xml
