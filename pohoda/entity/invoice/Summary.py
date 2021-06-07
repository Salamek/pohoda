# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.type.CurrencyForeign import CurrencyForeign
from pohoda.entity.type.CurrencyHome import CurrencyHome


class Summary(Agenda):
    _elements = ['roundingDocument', 'roundingVAT', 'homeCurrency', 'foreignCurrency']

    def __init__(self, data: dict, ico: str):

        home_currency = data.get('homeCurrency')
        if home_currency:
            data['homeCurrency'] = CurrencyHome(data['homeCurrency'], ico)

        foreign_currency = data.get('foreignCurrency')
        if foreign_currency:
            data['foreignCurrency'] = CurrencyForeign(data, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('invoiceSummary', namespace='inv')
        self._add_elements(xml, self._elements, 'inv')
        return xml
