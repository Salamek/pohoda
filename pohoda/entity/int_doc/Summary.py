# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.type.CurrencyForeign import CurrencyForeign
from pohoda.entity.type.CurrencyHome import CurrencyHome


class Summary(Agenda):
    _elements = ['roundingDocument', 'roundingVAT', 'calculateVAT', 'homeCurrency', 'foreignCurrency']

    def __init__(self, data: dict, ico: str):
        # process home currency
        home_currency = data.get('homeCurrency')
        if home_currency:
            data['homeCurrency'] = CurrencyHome(home_currency, ico)

        # process foreign currency
        foreign_currency = data.get('foreignCurrency')
        if foreign_currency:
            data['foreignCurrency'] = CurrencyForeign(foreign_currency, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('intDocSummary', 'int')
        self._add_elements(xml, self._elements, 'int')
        return xml
