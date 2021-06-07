# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda


class UserFilterName(Agenda):
    def get_xml(self) -> etree.Element:
        element = self._create_xml_tag('userFilterName', namespace='ftr')
        element.text = self._data['userFilterName']
        return element
