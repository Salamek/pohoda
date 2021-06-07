# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.cash_slip.Header import Header
from pohoda.entity.cash_slip.Item import Item
from pohoda.entity.cash_slip.Summary import Summary
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait


class CashSlip(Agenda, AddParameterToHeaderTrait):
    import_root = 'lst:prodejka'

    def __init__(self, data: dict, ico: str):
        data = {
            'header': Header(data, ico)
        }
        super().__init__(data, ico)

    def add_item(self, data: dict) -> 'CashSlip':
        """
        Add item.
        :param data:
        :return:
        """
        if not self._data.get('prodejkaDetail'):
            self._data['prodejkaDetail'] = []

        self._data['prodejkaDetail'].append(Item(data, self._ico))

        return self

    def add_summary(self, data: dict) -> 'CashSlip':
        """
        Add summary.
        :param data:
        :return:
        """

        self._data['summary'] = Summary(data, self._ico)
        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('prodejka', namespace='pro')
        xml.set('version', '2.0')
        self._add_elements(xml, ['header', 'prodejkaDetail', 'summary'], 'pro')
        return xml
