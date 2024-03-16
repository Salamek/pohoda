# coding: utf-8
from typing import List

from pohoda.entity.invoice.AdvancePaymentItem import AdvancePaymentItem

from pohoda.entity.Document import Document
from pohoda.entity.type.Link import Link


class Invoice(Document):
    import_root = 'lst:invoice'

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

    def _get_document_elements(self) -> List[str]:
        return ['links'] + super()._get_document_elements()

    def _get_document_namespace(self) -> str:
        return 'inv'

    def _get_document_name(self) -> str:
        return 'invoice'
