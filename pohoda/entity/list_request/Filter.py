# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda


class Filter(Agenda):
    _ref_elements = ['storage', 'store']
    _elements = ['id', 'code', 'EAN', 'name', 'storage', 'store', 'internet', 'company', 'ico', 'dic', 'lastChanges',
                 'dateFrom', 'dateTill']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('filter', namespace='ftr')
        self._add_elements(xml, self._elements, 'ftr')
        return xml
