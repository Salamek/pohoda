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


def test_can_set_action_type(stock: Stock) -> None:
    expected_xml = b"""<stk:stock xmlns:stk="http://www.stormware.cz/schema/version_2/stock.xsd" version="2.0">
  <stk:actionType>
    <stk:update>
      <ftr:filter xmlns:ftr="http://www.stormware.cz/schema/version_2/filter.xsd">
        <ftr:code>CODE</ftr:code>
        <ftr:store>
          <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">STORAGE</typ:ids>
        </ftr:store>
      </ftr:filter>
    </stk:update>
  </stk:actionType>
  <stk:stockHeader>
    """ + default_header + b"""
  </stk:stockHeader>
</stk:stock>
"""

    stock.add_action_type('update', {
        'code': 'CODE',
        'store': {
            'ids': 'STORAGE'
        }
    })

    result = bytes(etree.tostring(stock.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_set_prices(stock: Stock) -> None:
    stock.add_price('Price1', 20.43)
    stock.add_price('Price2', 19)

    expected_xml = b"""<stk:stock xmlns:stk="http://www.stormware.cz/schema/version_2/stock.xsd" version="2.0">
  <stk:stockHeader>
    """ + default_header + b"""
  </stk:stockHeader>
  <stk:stockPriceItem>
    <stk:stockPrice>
      <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">Price1</typ:ids>
      <typ:price xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">20.43</typ:price>
    </stk:stockPrice>
    <stk:stockPrice>
      <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">Price2</typ:ids>
      <typ:price xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">19</typ:price>
    </stk:stockPrice>
  </stk:stockPriceItem>
</stk:stock>
"""

    result = bytes(etree.tostring(stock.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_set_images(stock: Stock) -> None:
    expected_xml = b"""<stk:stock xmlns:stk="http://www.stormware.cz/schema/version_2/stock.xsd" version="2.0">
  <stk:stockHeader>
    """ + default_header + b"""
    <stk:pictures>
      <stk:picture default="false">
        <stk:filepath>image1.jpg</stk:filepath>
        <stk:order>1</stk:order>
      </stk:picture>
      <stk:picture default="true">
        <stk:filepath>image2.jpg</stk:filepath>
        <stk:description>NAME</stk:description>
        <stk:order>2</stk:order>
      </stk:picture>
    </stk:pictures>
  </stk:stockHeader>
</stk:stock>
"""

    stock.add_image('image1.jpg')
    stock.add_image('image2.jpg', 'NAME', None, True)

    result = bytes(etree.tostring(stock.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_set_categories(stock: Stock) -> None:
    expected_xml = b"""<stk:stock xmlns:stk="http://www.stormware.cz/schema/version_2/stock.xsd" version="2.0">
  <stk:stockHeader>
    """ + default_header + b"""
    <stk:categories>
      <stk:idCategory>1</stk:idCategory>
      <stk:idCategory>2</stk:idCategory>
    </stk:categories>
  </stk:stockHeader>
</stk:stock>
"""
    stock.add_category(1)
    stock.add_category(2)

    result = bytes(etree.tostring(stock.get_xml(), pretty_print=True))
    assert result == expected_xml


def can_set_int_parameters(stock: Stock) -> None:
    expected_xml = b"""<stk:stock xmlns:stk="http://www.stormware.cz/schema/version_2/stock.xsd" version="2.0">
  <stk:stockHeader>
    """ + default_header + b"""
    <stk:intParameters>
      <stk:intParameter>
        <stk:intParameterID>1</stk:intParameterID>
        <stk:intParameterType>numberValue</stk:intParameterType>
        <stk:intParameterValues>
          <stk:intParameterValue>
            <stk:parameterValue>VALUE1</stk:parameterValue>
          </stk:intParameterValue>
        </stk:intParameterValues>
      </stk:intParameter>
    </stk:intParameters>
  </stk:stockHeader>
</stk:stock>
"""
    stock.add_int_parameter({
        'intParameterID': 1,
        'intParameterType': 'numberValue',
        'value': 'VALUE1'
    })

    result = bytes(etree.tostring(stock.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_set_parameters(stock: Stock) -> None:
    expected_xml = b"""<stk:stock xmlns:stk="http://www.stormware.cz/schema/version_2/stock.xsd" version="2.0">
  <stk:stockHeader>
    """ + default_header + b"""
    <stk:parameters>
      <typ:parameter xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>IsOn</typ:name>
        <typ:booleanValue>true</typ:booleanValue>
      </typ:parameter>
      <typ:parameter xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>VPrNum</typ:name>
        <typ:numberValue>10.43</typ:numberValue>
      </typ:parameter>
      <typ:parameter xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>RefVPrCountry</typ:name>
        <typ:listValueRef>
          <typ:ids>SK</typ:ids>
        </typ:listValueRef>
        <typ:list>
          <typ:ids>Country</typ:ids>
        </typ:list>
      </typ:parameter>
      <typ:parameter xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>CustomList</typ:name>
        <typ:listValueRef>
          <typ:id>5</typ:id>
        </typ:listValueRef>
        <typ:list>
          <typ:id>6</typ:id>
        </typ:list>
      </typ:parameter>
    </stk:parameters>
  </stk:stockHeader>
</stk:stock>
"""
    stock.add_parameter('IsOn', 'boolean', 'true')
    stock.add_parameter('VPrNum', 'number', 10.43)
    stock.add_parameter('RefVPrCountry', 'list', 'SK', 'Country')
    stock.add_parameter('CustomList', 'list', {'id': 5}, {'id': 6})

    result = bytes(etree.tostring(stock.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_delete_stock() -> None:
    expected_xml = b"""<stk:stock xmlns:stk="http://www.stormware.cz/schema/version_2/stock.xsd" version="2.0">
  <stk:actionType>
    <stk:delete>
      <ftr:filter xmlns:ftr="http://www.stormware.cz/schema/version_2/filter.xsd">
        <ftr:code>CODE</ftr:code>
        <ftr:store>
          <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">STORAGE</typ:ids>
        </ftr:store>
      </ftr:filter>
    </stk:delete>
  </stk:actionType>
</stk:stock>
"""
    stock = Stock({}, '123')
    stock.add_action_type('delete', {
        'code': 'CODE',
        'store': {
            'ids': 'STORAGE'
        }
    })

    result = bytes(etree.tostring(stock.get_xml(), pretty_print=True))
    assert result == expected_xml
