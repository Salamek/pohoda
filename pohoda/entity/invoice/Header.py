# coding: utf-8
from pohoda.entity.document.Header import Header as DocumentHeader


class Header(DocumentHeader):
    _ref_elements = ['extId', 'number', 'accounting', 'classificationVAT', 'classificationKVDPH', 'order', 'paymentType', 'priceLevel', 'account', 'paymentAccount', 'centre', 'activity', 'contract', 'regVATinEU', 'MOSS', 'evidentiaryResourcesMOSS', 'carrier']
    _elements = ['extId', 'invoiceType', 'number', 'symVar', 'originalDocument', 'originalDocumentNumber', 'symPar', 'date', 'dateTax', 'dateAccounting', 'dateKHDPH', 'dateDue', 'dateApplicationVAT', 'dateDelivery', 'accounting', 'classificationVAT', 'classificationKVDPH', 'numberKHDPH', 'text', 'partnerIdentity', 'myIdentity', 'order', 'numberOrder', 'dateOrder', 'paymentType', 'priceLevel', 'account', 'symConst', 'symSpec', 'paymentAccount', 'paymentTerminal', 'centre', 'activity', 'contract', 'regVATinEU', 'MOSS', 'evidentiaryResourcesMOSS', 'accountingPeriodMOSS', 'dateTaxOriginalDocumentMOSS', 'note', 'carrier', 'intNote']

    def __init__(self, data: dict, ico: str):
        data.setdefault('invoiceType', 'issuedInvoice')
        super().__init__(data, ico)
