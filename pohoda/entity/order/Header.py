# coding: utf-8

from pohoda.entity.document.Header import Header as DocumentHeader


class Header(DocumentHeader):
    _ref_elements = ['extId', 'number', 'paymentType', 'priceLevel', 'centre', 'activity', 'contract', 'regVATinEU', 'MOSS', 'evidentiaryResourcesMOSS', 'carrier']
    _elements = ['extId', 'orderType', 'number', 'numberOrder', 'date', 'dateDelivery', 'dateFrom', 'dateTo', 'text', 'partnerIdentity', 'myIdentity', 'paymentType',
                 'priceLevel', 'isExecuted', 'isReserved', 'centre', 'activity', 'contract', 'regVATinEU', 'MOSS', 'evidentiaryResourcesMOSS', 'accountingPeriodMOSS',
                 'note', 'carrier', 'intNote', 'markRecord']

    def __init__(self, data: dict, ico: str):
        data.setdefault('orderType', 'receivedOrder')

        super().__init__(data, ico)
