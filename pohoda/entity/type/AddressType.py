# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda


class AddressType(Agenda):
    _ref_elements = ['country']
    _elements = ['company', 'division', 'name', 'city', 'street', 'zip', 'ico', 'dic', 'VATPayerType', 'icDph',
                 'country', 'phone', 'mobilPhone', 'fax', 'email']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('address', namespace='typ')
        self._add_elements(xml, self._elements, 'typ')
        return xml
