# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda


class Intrastat(Agenda):
    _elements = ['goodsCode', 'description', 'statistic', 'unit', 'coefficient', 'country']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('intrastat', namespace='stk')
        self._add_elements(xml, self._elements, 'stk')
        return xml
