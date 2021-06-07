# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.Address import Address
from pohoda.entity.type.MyAddress import MyAddress


class Header(Agenda, AddParameterTrait):
    _ref_elements = ['number', 'paymentType', 'priceLevel', 'centre', 'activity', 'contract', 'regVATinEU', 'carrier']
    _elements = ['orderType', 'number', 'numberOrder', 'date', 'dateDelivery', 'dateFrom', 'dateTo', 'text',
                 'partnerIdentity', 'myIdentity', 'paymentType', 'priceLevel', 'isExecuted', 'isReserved', 'centre',
                 'activity', 'contract', 'regVATinEU', 'note', 'carrier', 'intNote', 'markRecord']

    def __init__(self, data: dict, ico: str):
        # process partner identity
        partner_identity = data.get('partnerIdentity')
        if partner_identity:
            data['partnerIdentity'] = Address(partner_identity, ico)

        # process my identity
        my_identity = data.get('myIdentity')
        if my_identity:
            data['myIdentity'] = MyAddress(my_identity, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('orderHeader', namespace='ord')
        self._add_elements(xml, self._elements + ['parameters'], 'ord')
        return xml
