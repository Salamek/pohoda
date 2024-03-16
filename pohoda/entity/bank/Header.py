# coding: utf-8
from pohoda.entity.document.Header import Header as DocumentHeader
from pohoda.entity.bank.StatementNumber import StatementNumber


class Header(DocumentHeader):
    _ref_elements = ['account', 'accounting', 'classificationVAT', 'classificationKVDPH', 'paymentAccount', 'centre', 'activity', 'contract', 'MOSS',
                     'evidentiaryResourcesMOSS']
    _elements = ['bankType', 'account', 'statementNumber', 'symVar', 'dateStatement', 'datePayment', 'accounting', 'classificationVAT', 'classificationKVDPH', 'text',
                 'partnerIdentity', 'myIdentity', 'paymentAccount', 'symConst', 'symSpec', 'symPar', 'centre', 'activity', 'contract', 'MOSS', 'evidentiaryResourcesMOSS',
                 'accountingPeriodMOSS', 'note', 'intNote']

    def __init__(self, data: dict, ico: str):
        statement_number = data.get('statementNumber')
        if statement_number:
            data['statementNumber'] = StatementNumber(statement_number, ico)

        super().__init__(data, ico)
