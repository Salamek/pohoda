import pytest
import datetime
from lxml import etree

from pohoda.entity.Agenda import Agenda
from pohoda.entity.Supplier import Supplier


@pytest.fixture(scope="function")  # type: ignore
def supplier() -> Supplier:
    return Supplier({
        'stockItem': {
            'stockItem': {
                'ids': 'B04'
            }
        },
        'suppliers': [
            {
                'supplierItem': {
                    'default': True,
                    'refAd': {
                        'id': 2
                    },
                    'orderCode': 'A1',
                    'orderName': 'A-zasoba',
                    'purchasingPrice': 1968,
                    'rate': 0,
                    'payVAT': False,
                    'ean': '11112228',
                    'printEAN': True,
                    'unitEAN': 'ks',
                    'unitCoefEAN': 1,
                    'deliveryTime': 12,
                    'minQuantity': 2,
                    'note': 'fdf'
                }
            },
            {
                'supplierItem': {
                    'default': False,
                    'refAd': {
                        'ids': 'INTEAK spol. s r. o.'
                    },
                    'orderCode': 'I1',
                    'orderName': 'I-zasoba',
                    'purchasingPrice': 500,
                    'rate': 0,
                    'payVAT': False,
                    'ean': '212121212',
                    'printEAN': True,
                    'unitEAN': 'ks',
                    'unitCoefEAN': 1,
                    'deliveryTime': 12,
                    'minQuantity': 2,
                    'note': 'aasn'
                }
            }
        ]
    }, '123')


def test_be_constructed_with() -> None:
    Supplier({
        'stockItem': {
            'stockItem': {
                'ids': 'B04'
            }
        },
        'suppliers': [
            {
                'supplierItem': {
                    'default': True,
                    'refAd': {
                        'id': 2
                    },
                    'orderCode': 'A1',
                    'orderName': 'A-zasoba',
                    'purchasingPrice': 1968,
                    'rate': 0,
                    'payVAT': False,
                    'ean': '11112228',
                    'printEAN': True,
                    'unitEAN': 'ks',
                    'unitCoefEAN': 1,
                    'deliveryTime': 12,
                    'minQuantity': 2,
                    'note': 'fdf'
                }
            },
            {
                'supplierItem': {
                    'default': False,
                    'refAd': {
                        'ids': 'INTEAK spol. s r. o.'
                    },
                    'orderCode': 'I1',
                    'orderName': 'I-zasoba',
                    'purchasingPrice': 500,
                    'rate': 0,
                    'payVAT': False,
                    'ean': '212121212',
                    'printEAN': True,
                    'unitEAN': 'ks',
                    'unitCoefEAN': 1,
                    'deliveryTime': 12,
                    'minQuantity': 2,
                    'note': 'aasn'
                }
            }
        ]
    }, '123')


def test_extends_agenda(supplier: Supplier) -> None:
    assert isinstance(supplier, Supplier)
    assert isinstance(supplier, Agenda)


def test_creates_correct_xml(supplier: Supplier) -> None:
    expected_xml = b"""<sup:supplier xmlns:sup="http://www.stormware.cz/schema/version_2/supplier.xsd" version="2.0">
  <sup:stockItem>
    <typ:stockItem xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
      <typ:ids>B04</typ:ids>
    </typ:stockItem>
  </sup:stockItem>
  <sup:suppliers>
    <sup:supplierItem default="true">
      <sup:refAd>
        <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">2</typ:id>
      </sup:refAd>
      <sup:orderCode>A1</sup:orderCode>
      <sup:orderName>A-zasoba</sup:orderName>
      <sup:purchasingPrice>1968</sup:purchasingPrice>
      <sup:rate>0</sup:rate>
      <sup:payVAT>false</sup:payVAT>
      <sup:ean>11112228</sup:ean>
      <sup:printEAN>true</sup:printEAN>
      <sup:unitEAN>ks</sup:unitEAN>
      <sup:unitCoefEAN>1</sup:unitCoefEAN>
      <sup:deliveryTime>12</sup:deliveryTime>
      <sup:minQuantity>2</sup:minQuantity>
      <sup:note>fdf</sup:note>
    </sup:supplierItem>
    <sup:supplierItem default="false">
      <sup:refAd>
        <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">INTEAK spol. s r. o.</typ:ids>
      </sup:refAd>
      <sup:orderCode>I1</sup:orderCode>
      <sup:orderName>I-zasoba</sup:orderName>
      <sup:purchasingPrice>500</sup:purchasingPrice>
      <sup:rate>0</sup:rate>
      <sup:payVAT>false</sup:payVAT>
      <sup:ean>212121212</sup:ean>
      <sup:printEAN>true</sup:printEAN>
      <sup:unitEAN>ks</sup:unitEAN>
      <sup:unitCoefEAN>1</sup:unitCoefEAN>
      <sup:deliveryTime>12</sup:deliveryTime>
      <sup:minQuantity>2</sup:minQuantity>
      <sup:note>aasn</sup:note>
    </sup:supplierItem>
  </sup:suppliers>
</sup:supplier>
"""

    result = bytes(etree.tostring(supplier.get_xml(), pretty_print=True))
    assert result == expected_xml
