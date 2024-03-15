from lxml import etree
from pohoda.entity.Agenda import Agenda


class StockItem(Agenda):
    _ref_elements = ['stockItem']
    _elements = ['stockItem']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('stockItem', namespace='sup')
        self._add_elements(xml, self._elements, 'typ')
        return xml

