# coding: utf-8

from pohoda.entity.Agenda import Agenda


class Price(Agenda):
    def get_xml(self):
        xml = self._create_xml_tag('stockPriceItem', namespace='stk')
        return self._add_ref_element(xml, 'stockPrice', {
            'ids': self._data['code'],
            'price': self._data['value']
        }, namespace='stk')
