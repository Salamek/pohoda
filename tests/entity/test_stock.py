import pytest
from lxml import etree

from pohoda.entity.Agenda import Agenda
from pohoda.entity.Stock import Stock

default_header = b"""<stk:stockType>card</stk:stockType>
    <stk:code>CODE</stk:code>
    <stk:isSales>false</stk:isSales>
    <stk:isSerialNumber>false</stk:isSerialNumber>
    <stk:isInternet>true</stk:isInternet>
    <stk:name>NAME</stk:name>
    <stk:storage>
      <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">STORAGE</typ:ids>
    </stk:storage>
    <stk:typePrice>
      <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">1</typ:id>
    </stk:typePrice>
    <stk:sellingPrice payVAT="true">12.7</stk:sellingPrice>
    <stk:intrastat>
      <stk:goodsCode>123</stk:goodsCode>
      <stk:unit>ZZZ</stk:unit>
      <stk:coefficient>0</stk:coefficient>
      <stk:country>CN</stk:country>
    </stk:intrastat>
    <stk:recyclingContrib>
      <stk:recyclingContribType>
        <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">X</typ:ids>
      </stk:recyclingContribType>
      <stk:coefficientOfRecyclingContrib>1</stk:coefficientOfRecyclingContrib>
    </stk:recyclingContrib>"""


@pytest.fixture(scope="function")  # type: ignore
def stock() -> Stock:
    return Stock({
        'code': 'CODE',
        'name': 'NAME',
        'isSales': False,
        'isSerialNumber': 'false',
        'isInternet': True,
        'storage': 'STORAGE',
        'typePrice': {
            'id': 1
        },
        'sellingPrice': 12.7,
        'sellingPricePayVAT': True,
        'intrastat': {
            'goodsCode': '123',
            'unit': 'ZZZ',
            'coefficient': 0,
            'country': 'CN'
        },
        'recyclingContrib': {
            'recyclingContribType': 'X',
            'coefficientOfRecyclingContrib': 1
        }
    }, '123')


def test_be_constructed_with() -> None:
    Stock({
        'code': 'CODE',
        'name': 'NAME',
        'isSales': False,
        'isSerialNumber': 'false',
        'isInternet': True,
        'storage': 'STORAGE',
        'typePrice': {
            'id': 1
        },
        'sellingPrice': 12.7,
        'sellingPricePayVAT': True,
        'intrastat': {
            'goodsCode': '123',
            'unit': 'ZZZ',
            'coefficient': 0,
            'country': 'CN'
        },
        'recyclingContrib': {
            'recyclingContribType': 'X',
            'coefficientOfRecyclingContrib': 1
        }
    }, '123')


def test_extends_agenda(stock: Stock) -> None:
    assert isinstance(stock, Agenda)


def test_creates_correct_xml(stock: Stock) -> None:
    expected_xml = b"""<stk:stock xmlns:stk="http://www.stormware.cz/schema/version_2/stock.xsd" version="2.0">
  <stk:stockHeader>
    """ + default_header + b"""
  </stk:stockHeader>
</stk:stock>
"""

    result = bytes(etree.tostring(stock.get_xml(), pretty_print=True))
    assert result == expected_xml


