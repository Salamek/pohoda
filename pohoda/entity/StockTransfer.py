# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.stock_transfer.Header import Header
from pohoda.entity.stock_transfer.Item import Item


class StockTransfer(Agenda, AddParameterToHeaderTrait):
    import_root = 'lst:prevodka'

    def __init__(self, data: dict, ico: str):
        data = {'header': Header(data, ico)}
        super().__init__(data, ico)

    def add_item(self, data: dict) -> 'StockTransfer':
        """
        Add item.
        :param data:
        :return:
        """

        if not self._data.get('prevodkaDetail'):
            self._data['prevodkaDetail'] = []

        self._data['prevodkaDetail'].append(Item(data, self._ico))
        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('prevodka', namespace='pre')
        xml.set('version', '2.0')
        self._add_elements(xml, ['header', 'prevodkaDetail'], 'pre')
        return xml
