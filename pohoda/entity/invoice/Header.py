# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.Address import Address
from pohoda.entity.type.MyAddress import MyAddress


class Header(Agenda, AddParameterTrait):
    _ref_elements = ['number', 'accounting', 'classificationVAT', 'classificationKVDPH', 'order', 'paymentType',
                     'priceLevel', 'account', 'paymentAccount', 'centre', 'activity', 'contract', 'regVATinEU',
                     'carrier']
    _elements = ['extId', 'invoiceType', 'number', 'symVar', 'originalDocument', 'originalDocumentNumber', 'symPar',
                 'date', 'dateTax', 'dateAccounting', 'dateKHDPH', 'dateDue', 'dateApplicationVAT', 'dateDelivery',
                 'accounting', 'classificationVAT', 'classificationKVDPH', 'numberKHDPH', 'text', 'partnerIdentity',
                 'myIdentity', 'order', 'numberOrder', 'dateOrder', 'paymentType', 'priceLevel', 'account', 'symConst',
                 'symSpec', 'paymentAccount', 'paymentTerminal', 'centre', 'activity', 'contract', 'regVATinEU', 'note',
                 'carrier', 'intNote']

    def __init__(self, data: dict, ico: str):
        partner_identity = data.get('partnerIdentity')
        if partner_identity:
            data['partnerIdentity'] = Address(partner_identity, ico)

        my_identity = data.get('myIdentity')
        if my_identity:
            data['myIdentity'] = MyAddress(my_identity, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml_ = self._create_xml_tag('invoiceHeader', namespace='inv')
        self._add_elements(xml_, self._elements + ['parameters'], 'inv')
        return xml_
