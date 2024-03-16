# coding: utf-8
from pohoda.entity.document.Item import Item as DocumentItem


class Item(DocumentItem):
    _ref_elements = ['typeServiceMOSS', 'accounting', 'classificationVAT', 'classificationKVDPH', 'centre', 'activity', 'contract']
    _elements = ['text', 'quantity', 'unit', 'coefficient', 'payVAT', 'rateVAT', 'discountPercentage', 'homeCurrency', 'foreignCurrency', 'typeServiceMOSS', 'note', 'symPar', 'accounting', 'classificationVAT', 'classificationKVDPH', 'centre', 'activity', 'contract']


