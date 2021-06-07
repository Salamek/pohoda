# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class Category(Agenda):
    def get_xml(self) -> etree.Element:
        element = self._create_xml_tag('idCategory', namespace='stk')
        element.text = self._data['idCategory']
        return element
