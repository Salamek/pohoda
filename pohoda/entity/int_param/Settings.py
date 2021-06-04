# coding: utf-8

from pohoda.entity.Agenda import Agenda


class Settings(Agenda):
    _ref_elements = ['currency']
    _elements = ['unit', 'length', 'currency', 'parameterList']

    def get_xml(self):
        xml = self._create_xml_tag('parameterSettings', namespace='ipm')
        self._add_elements(xml, self._elements, 'ipm')
        return xml
