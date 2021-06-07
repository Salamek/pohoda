# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda


class Picture(Agenda):

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('picture', namespace='stk')
        xml.set('default', self._data['default'])
        self._add_elements(xml, ['filepath', 'description', 'order'], 'stk')
        return xml
