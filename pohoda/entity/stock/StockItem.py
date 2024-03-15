# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.stock.Price import Price


class StockItem(Agenda):
    _ref_elements = ['stockInfo', 'storage']
    _elements = ['id', 'stockInfo', 'storage', 'code', 'name', 'count', 'quantity', 'stockPriceItem']

    def __init__(self, data: dict, ico: str):

        # process stockPriceItem
        stock_price_item = data.get('stockPriceItem')
        if stock_price_item:
            data['stockPriceItem'] = [Price(supplier['stockPrice'], ico) for supplier in stock_price_item]
        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('stockItem', namespace='stk')
        self._add_elements(xml, self._elements, 'stk')
        return xml

