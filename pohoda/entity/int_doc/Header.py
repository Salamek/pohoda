# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.Address import Address
from pohoda.entity.type.MyAddress import MyAddress


class Header(Agenda, AddParameterTrait):
    _ref_elements = ['number', 'accounting', 'classificationVAT', 'classificationKVDPH', 'centre', 'activity',
                     'contract', 'regVATinEU']
    _elements = ['number', 'symVar', 'symPar', 'originalDocumentNumber', 'originalCorrectiveDocument', 'date',
                 'dateTax', 'dateAccounting', 'dateDelivery', 'dateKVDPH', 'dateKHDPH', 'accounting',
                 'classificationVAT', 'classificationKVDPH', 'numberKHDPH', 'text', 'partnerIdentity', 'myIdentity',
                 'liquidation', 'centre', 'activity', 'contract', 'regVATinEU', 'note', 'intNote', 'markRecord']

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
        xml = self._create_xml_tag('intDocHeader', namespace='int')
        self._add_elements(xml, self._elements + ['parameters'], 'int')
        return xml
