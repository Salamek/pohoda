# coding: utf-8

from pohoda.entity.Agenda import Agenda


class Report(Agenda):
    _elements = ['id']

    def get_xml(self):
        xml = self._create_xml_tag('report', namespace='prn')
        self._add_elements(xml, self._elements, 'prn')
        return xml
