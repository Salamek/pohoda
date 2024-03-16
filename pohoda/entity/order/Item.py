# coding: utf-8
from pohoda.entity.document.Item import Item as DocumentItem


class Item(DocumentItem):
    _ref_elements = ['typeServiceMOSS', 'centre', 'activity', 'contract']
    _elements = ['text', 'quantity', 'delivered', 'unit', 'coefficient', 'payVAT', 'rateVAT', 'percentVAT', 'discountPercentage', 'homeCurrency', 'foreignCurrency',
                 'typeServiceMOSS', 'note', 'code', 'stockItem', 'centre', 'activity', 'contract', 'PDP']
