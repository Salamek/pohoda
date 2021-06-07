# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.receipt.Header import Header
from pohoda.entity.receipt.Item import Item


class Receipt(Agenda, AddParameterToHeaderTrait):
    import_root = 'lst:prijemka'

    def __init__(self, data: dict, ico: str):
        data = {'header': Header(data, ico)}
        super().__init__(data, ico)

    def add_item(self, data: dict) -> 'Receipt':
        """
        Add item.
        :param data:
        :return:
        """

        if not self._data.get('prijemkaDetail'):
            self._data['prijemkaDetail'] = []

        self._data['prijemkaDetail'].append(Item(data, self._ico))
        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('prijemka', namespace='pri')
        xml.set('version', '2.0')
        self._add_elements(xml, ['header', 'prijemkaDetail', 'summary'], 'pri')
        return xml
