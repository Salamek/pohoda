# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.SetNamespaceTrait import SetNamespaceTrait
from pohoda.entity.common.SetNodeNameTrait import SetNodeNameTrait
from pohoda.entity.type.AddressType import AddressType
from pohoda.entity.type.ShipToAddressType import ShipToAddressType


class Address(Agenda, SetNamespaceTrait, SetNodeNameTrait):
    _ref_elements = ['extId']
    _elements = ['id', 'extId', 'address', 'addressLinkToAddress', 'shipToAddress']

    _elements_attributes_mapper = {'addressLinkToAddress': ['address', 'linkToAddress']}

    def __init__(self, data: dict, ico: str):
        address = data.get('address')
        if address:
            data['address'] = AddressType(address, ico)

        ship_to_address = data.get('shipToAddress')
        if ship_to_address:
            data['shipToAddress'] = ShipToAddressType(data['shipToAddress'], ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:

        if not self._namespace:
            raise ValueError('Namespace not set.')

        if not self._node_name:
            raise ValueError('Node name not set.')

        xml = self._create_xml_tag(self._node_name, namespace=self._namespace)
        self._add_elements(xml, self._elements, 'typ')
        return xml
