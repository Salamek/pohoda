# coding: utf-8

from pohoda.entity.Agenda import Agenda


class UserFilterName(Agenda):
    def get_xml(self):
        element = self._create_xml_tag('userFilterName', namespace='ftr')
        element.text = self._data['userFilterName']
        return element
