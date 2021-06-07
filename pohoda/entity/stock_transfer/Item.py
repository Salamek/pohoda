# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.type.StockItem import StockItem


class Item(Agenda):
    _elements = ['quantity', 'stockItem', 'note']

    def __init__(self, data: dict, ico: str):
        # process stock item
        stock_item = data.get('stockItem')
        if stock_item:
            data['stockItem'] = StockItem(stock_item, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('prevodkaItem', namespace='pre')
        self._add_elements(xml, self._elements, 'pre')
        return xml
