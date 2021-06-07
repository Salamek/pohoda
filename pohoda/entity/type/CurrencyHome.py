# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.SetNamespaceTrait import SetNamespaceTrait
from pohoda.entity.common.SetNodeNameTrait import SetNodeNameTrait


class CurrencyHome(Agenda, SetNamespaceTrait, SetNodeNameTrait):
    _ref_elements = ['round']
    _elements = ['priceNone', 'price3', 'price3VAT', 'price3Sum', 'priceLow', 'priceLowVAT', 'priceLowSum', 'priceHigh',
                 'priceHighVAT', 'priceHighSum', 'round']

    def get_xml(self) -> etree.Element:

        if not self._namespace:
            raise ValueError('Namespace not set.')

        if not self._node_name:
            raise ValueError('Node name not set.')
        # end if
        xml = self._create_xml_tag(self._node_name, self._namespace)
        self._add_elements(xml, self._elements, 'typ')
        return xml
