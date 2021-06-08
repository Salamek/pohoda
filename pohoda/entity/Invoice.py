# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.invoice.AdvancePaymentItem import AdvancePaymentItem
from pohoda.entity.invoice.Header import Header
from pohoda.entity.invoice.Item import Item
from pohoda.entity.invoice.Summary import Summary
from pohoda.entity.type.Link import Link


class Invoice(Agenda, AddParameterToHeaderTrait):
    import_root = 'lst:invoice'

    def __init__(self, data: dict, ico: str):

        if 'invoiceType' not in data:
            data['invoiceType'] = 'issuedInvoice'

        data = {'header': Header(data, ico)}
        super().__init__(data, ico)

    def add_link(self, data: dict) -> 'Invoice':
        """
        Add link.
        :param data:
        :return:
        """
        if not self._data.get('links'):
            self._data['links'] = []

        self._data['links'].append(Link(data, self._ico))

        return self

    def add_item(self, data: dict) -> 'Invoice':
        """
        Add invoice item.
        :param data:
        :return:
        """

        if not self._data.get('invoiceDetail'):
            self._data['invoiceDetail'] = []

        self._data['invoiceDetail'].append(Item(data, self._ico))
        return self

    def add_advance_payment_item(self, data: dict) -> 'Invoice':
        """
        Add advance payment item.
        :param data:
        :return:
        """

        if not self._data.get('invoiceDetail'):
            self._data['invoiceDetail'] = []

        self._data['invoiceDetail'].append(AdvancePaymentItem(data, self._ico))
        return self

    def add_summary(self, data: dict) -> 'Invoice':
        """
        Add invoice summary.
        :param data:
        :return:
        """

        self._data['summary'] = Summary(data, self._ico)
        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('invoice', namespace='inv')
        xml.set('version', '2.0')
        self._add_elements(xml, ['links', 'header', 'invoiceDetail', 'summary'], 'inv')
        return xml
