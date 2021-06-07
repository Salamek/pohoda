# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.Address import Address


class Desc(Agenda, AddParameterTrait):
    _ref_elements = ['number', 'responsiblePerson']

    _elements = ['number', 'datePlanStart', 'datePlanDelivery', 'dateStart', 'dateDelivery', 'dateWarranty', 'text',
                 'partnerIdentity', 'responsiblePerson', 'note']

    def __init__(self, data: dict, ico: str):
        # process partner identity
        partner_identity = data.get('partnerIdentity')
        if partner_identity:
            data['partnerIdentity'] = Address(partner_identity, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('contractDesc', namespace='con')
        self._add_elements(xml, self._elements + ['parameters'], 'con')
        return xml
