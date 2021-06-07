# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda


class ShipToAddressType(Agenda):
    _ref_elements = ['country']
    _elements = ['company', 'division', 'name', 'city', 'street', 'zip', 'country', 'phone', 'email',
                 'defaultShipAddress']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('shipToAddress', namespace='typ')
        self._add_elements(xml, self._elements, 'typ')
        return xml
