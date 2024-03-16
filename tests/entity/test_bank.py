import pytest
import datetime
from lxml import etree

from pohoda.entity.Agenda import Agenda
from pohoda.entity.Bank import Bank


default_header = b"""
    <bnk:bankType>receipt</bnk:bankType>
    <bnk:account>
      <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">KB</typ:ids>
    </bnk:account>
    <bnk:statementNumber>
      <bnk:statementNumber>004</bnk:statementNumber>
      <bnk:numberMovement>0002</bnk:numberMovement>
    </bnk:statementNumber>
    <bnk:symVar>456</bnk:symVar>
    <bnk:dateStatement>2021-12-20</bnk:dateStatement>
    <bnk:datePayment>2021-11-22</bnk:datePayment>
    <bnk:text>STORMWARE s.r.o.</bnk:text>
    <bnk:paymentAccount>
      <typ:accountNo xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">4660550217</typ:accountNo>
      <typ:bankCode xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">5500</typ:bankCode>
    </bnk:paymentAccount>
    <bnk:symConst>555</bnk:symConst>
    <bnk:symSpec>666</bnk:symSpec>
  """


@pytest.fixture(scope="function")  # type: ignore
def bank() -> Bank:
    return Bank({
        'bankType': 'receipt',
        'account': 'KB',
        'statementNumber': {
            'statementNumber': '004',
            'numberMovement': '0002'
        },
        'symVar': '456',
        'symConst': '555',
        'symSpec': '666',
        'dateStatement': '2021-12-20',
        'datePayment': '2021-11-22',
        'text': 'STORMWARE s.r.o.',
        'paymentAccount': {
            'accountNo': '4660550217',
            'bankCode': '5500'
        }
    }, '123')


def test_be_constructed_with() -> None:
    Bank({
        'bankType': 'receipt',
        'account': 'KB',
        'statementNumber': {
            'statementNumber': '004',
            'numberMovement': '0002'
        },
        'symVar': '456',
        'symConst': '555',
        'symSpec': '666',
        'dateStatement': '2021-12-20',
        'datePayment': '2021-11-22',
        'text': 'STORMWARE s.r.o.',
        'paymentAccount': {
            'accountNo': '4660550217',
            'bankCode': '5500'
        }
    }, '123')


def test_extends_agenda(bank: Bank) -> None:
    assert isinstance(bank, Bank)
    assert isinstance(bank, Agenda)


def test_creates_correct_xml(bank: Bank) -> None:
    expected_xml = b"""<bnk:bank xmlns:bnk="http://www.stormware.cz/schema/version_2/bank.xsd" version="2.0">
  <bnk:bankHeader>""" + default_header + b"""</bnk:bankHeader>
</bnk:bank>
"""

    result = bytes(etree.tostring(bank.get_xml(), pretty_print=True))
    assert result == expected_xml
