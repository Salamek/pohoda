# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.type.StockItem import StockItem


class Item(Agenda):
    _ref_elements = ['centre', 'activity', 'contract']
    _elements = ['quantity', 'unit', 'coefficient', 'payVAT', 'rateVAT', 'discountPercentage', 'homeCurrency',
                 'foreignCurrency', 'code', 'stockItem', 'note', 'centre', 'activity', 'contract']

    def __init__(self, data: dict, ico: str):
        # process stock item
        stock_item = data.get('stockItem')
        if stock_item:
            data['stockItem'] = StockItem(stock_item, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('prijemkaItem', namespace='pri')
        self._add_elements(xml, self._elements, 'pri')
        return xml
