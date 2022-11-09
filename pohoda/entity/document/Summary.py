# coding: utf-8
from lxml import etree
from pohoda.entity.document.Part import Part
from pohoda.entity.type.CurrencyForeign import CurrencyForeign
from pohoda.entity.type.CurrencyHome import CurrencyHome


class Summary(Part):

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
        if not self._namespace:
            raise ValueError('Namespace not set.')

        if not self._node_prefix:
            raise ValueError('Node name prefix not set.')

        xml = self._create_xml_tag('{}Summary'.format(self._node_prefix), namespace=self._namespace)
        self._add_elements(xml, self._elements, self._namespace)
        return xml
