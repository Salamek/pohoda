# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.supplier.StockItem import StockItem
from pohoda.entity.supplier.SupplierItem import SupplierItem


class Supplier(Agenda):
    import_root = 'lst:supplier'

    def __init__(self, data: dict, ico: str):
        stock_item = data.get('stockItem')
        if stock_item:
            data['stockItem'] = StockItem(stock_item, ico)

        suppliers = data.get('suppliers')
        if suppliers:
            # Process suppliers
            data['suppliers'] = [SupplierItem(supplier['supplierItem'], ico) for supplier in suppliers]

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('supplier', namespace='sup')
        xml.set('version', '2.0')
        self._add_elements(xml, ['stockItem', 'suppliers'], 'sup')
        return xml

