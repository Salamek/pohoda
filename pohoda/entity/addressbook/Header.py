# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.Address import Address


class Header(Agenda, AddParameterTrait):
    _ref_elements = ['centre', 'activity', 'contract', 'number']

    _elements = ['identity', 'region', 'phone', 'mobil', 'fax', 'email', 'web', 'ICQ', 'Skype', 'GPS', 'credit',
                 'priceIDS', 'maturity', 'paymentType', 'agreement', 'number', 'ost1', 'ost2', 'p1', 'p2', 'p3', 'p4',
                 'p5', 'p6', 'message', 'note', 'intNote', 'centre', 'activity', 'contract']

    def __init__(self, data: dict, ico: str):
        identity = data.get('identity')
        if identity:
            data['identity'] = Address(identity, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('addressbookHeader', namespace='adb')
        self._add_elements(xml, self._elements + ['parameters'], 'adb')
        return xml
