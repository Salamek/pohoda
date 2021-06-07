# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddActionTypeTrait import AddActionTypeTrait
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.order.Header import Header
from pohoda.entity.order.Item import Item
from pohoda.entity.order.Summary import Summary


class Order(Agenda, AddActionTypeTrait, AddParameterToHeaderTrait):
    import_root = 'lst:order'

    def __init__(self, data: dict, ico: str):
        if data:
            data = {'header': Header(data, ico)}

        super().__init__(data, ico)

    def add_item(self, data: dict) -> 'Order':
        """
        Add order item.
        :param data:
        :return:
        """

        if not self._data.get('orderDetail'):
            self._data['orderDetail'] = []

        self._data['orderDetail'].append(Item(data, self._ico))
        return self

    def add_summary(self, data: dict) -> 'Order':
        """
        Add order summary.
        :param data:
        :return:
        """

        self._data['summary'] = Summary(data, self._ico)
        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('order', namespace='ord')
        xml.set('version', '2.0')
        self._add_elements(xml, ['actionType', 'header', 'orderDetail', 'summary'], 'ord')
        return xml
