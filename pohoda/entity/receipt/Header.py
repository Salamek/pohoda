# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.Address import Address


class Header(Agenda, AddParameterTrait):
    _ref_elements = ['number', 'centre', 'activity', 'contract']
    _elements = ['number', 'date', 'text', 'partnerIdentity', 'symPar', 'centre', 'activity', 'contract', 'note',
                 'intNote']

    def __init__(self, data: dict, ico: str):
        # process partner identity
        partner_identity = data.get('partnerIdentity')
        if partner_identity:
            data['partnerIdentity'] = Address(partner_identity, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('prijemkaHeader', namespace='pri')
        self._add_elements(xml, self._elements + ['parameters'], 'pri')
        return xml
