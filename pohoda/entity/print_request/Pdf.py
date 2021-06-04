# coding: utf-8

from pohoda.entity.Agenda import Agenda


class Pdf(Agenda):
    _elements = ['fileName']

    def get_xml(self):
        xml = self._create_xml_tag('pdf', namespace='prn')
        self._add_elements(xml, self._elements, 'prn')
        return xml
