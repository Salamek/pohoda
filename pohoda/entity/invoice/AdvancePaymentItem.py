# coding: utf-8
from lxml import etree
from pohoda.entity.invoice.Item import Item


class AdvancePaymentItem(Item):
    _ref_elements = ['sourceDocument', 'accounting', 'classificationVAT', 'classificationKVDPH', 'centre', 'activity',
                     'contract']
    _elements = ['sourceDocument', 'quantity', 'payVAT', 'rateVAT', 'discountPercentage', 'homeCurrency',
                 'foreignCurrency', 'note', 'accounting', 'classificationVAT', 'classificationKVDPH', 'centre',
                 'activity', 'contract']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('invoiceAdvancePaymentItem', namespace='inv')
        self._add_elements(xml, self._elements + ['parameters'], 'inv')
        return xml
