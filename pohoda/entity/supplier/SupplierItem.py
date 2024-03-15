from lxml import etree
from pohoda.entity.Agenda import Agenda


class SupplierItem(Agenda):
    _ref_elements = ['refAd', 'currency', 'deliveryPeriod']
    _elements = ['default', 'refAd', 'orderCode', 'orderName', 'purchasingPrice', 'currency', 'rate', 'payVAT', 'ean', 'printEAN', 'unitEAN', 'unitCoefEAN', 'deliveryTime', 'deliveryPeriod', 'minQuantity', 'unit', 'note']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('supplierItem', namespace='sup')

        if 'default' in self._data:
            xml.set('default', self._element_data_to_xml(self._data.get('default')))
            del self._data['default']
        self._add_elements(xml, self._elements, 'sup')
        return xml
