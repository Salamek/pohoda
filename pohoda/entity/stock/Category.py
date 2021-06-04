# coding: utf-8

from pohoda.entity.Agenda import Agenda


class Category(Agenda):
    def get_xml(self):
        element = self._create_xml_tag('idCategory', namespace='stk')
        element.text = self._data['idCategory']
        return element
