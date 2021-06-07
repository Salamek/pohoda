# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.CurrencyItem import CurrencyItem
from pohoda.entity.type.StockItem import StockItem


class Item(Agenda, AddParameterTrait):
    _ref_elements = ['centre', 'activity', 'contract']

    _elements = ['text', 'quantity', 'unit', 'coefficient', 'payVAT', 'rateVAT', 'discountPercentage', 'homeCurrency',
                 'foreignCurrency', 'note', 'code', 'stockItem', 'centre', 'activity', 'contract']

    def __init__(self, data: dict, ico: str):
        # process home currency
        home_currency = data.get('homeCurrency')
        if home_currency:
            data['homeCurrency'] = CurrencyItem(home_currency, ico)

        # process foreign currency
        foreign_currency = data.get('foreignCurrency')
        if foreign_currency:
            data['foreignCurrency'] = CurrencyItem(foreign_currency, ico)

        # process stock item
        stock_item = data.get('stockItem')
        if stock_item:
            data['stockItem'] = StockItem(stock_item, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('prodejkaItem', namespace='pro')
        self._add_elements(xml, self._elements + ['parameters'], 'pro')
        return xml
