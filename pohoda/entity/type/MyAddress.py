# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.SetNamespaceTrait import SetNamespaceTrait
from pohoda.entity.common.SetNodeNameTrait import SetNodeNameTrait
from pohoda.entity.type.AddressInternetType import AddressInternetType
from pohoda.entity.type.EstablishmentType import EstablishmentType


class MyAddress(Agenda, SetNamespaceTrait, SetNodeNameTrait):
    _elements = ['address', 'establishment']

    def __init__(self, data: dict, ico: str):
        address = data.get('address')
        if address:
            data['address'] = AddressInternetType(address, ico)

        establishment = data.get('establishment')
        if establishment:
            data['establishment'] = EstablishmentType(data['establishment'], ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        if not self._namespace:
            raise ValueError('Namespace not set.')

        if not self._node_name:
            raise ValueError('Node name not set.')

        xml = self._create_xml_tag(self._node_name, namespace=self._namespace)
        self._add_elements(xml, self._elements, 'typ')
        return xml
