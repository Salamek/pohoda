import pytest
import datetime
from lxml import etree

from pohoda.entity.Agenda import Agenda
from pohoda.entity.Invoice import Invoice


@pytest.fixture(scope="function")  # type: ignore
def invoice() -> Invoice:
    return Invoice({
        'partnerIdentity': {
            'id': 25
        },
        'myIdentity': {
            'address': {
                'name': 'NAME',
                'ico': '123'
            }
        },
        'date': datetime.date(year=2015, month=1, day=10),
        'intNote': 'Note'
    }, '123')


def test_be_constructed_with() -> None:
    Invoice({
        'partnerIdentity': {
            'id': 25
        },
        'myIdentity': {
            'address': {
                'name': 'NAME',
                'ico': '123'
            }
        },
        'date': datetime.date(year=2015, month=1, day=10),
        'intNote': 'Note'
    }, '123')


def test_extends_agenda(invoice: Invoice) -> None:
    assert isinstance(invoice, Agenda)


def test_creates_correct_xml(invoice: Invoice) -> None:
    expected_xml = b"""<inv:invoice xmlns:inv="http://www.stormware.cz/schema/version_2/invoice.xsd" version="2.0">
  <inv:invoiceHeader>
    <inv:invoiceType>issuedInvoice</inv:invoiceType>
    <inv:date>2015-01-10</inv:date>
    <inv:partnerIdentity>
      <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">25</typ:id>
    </inv:partnerIdentity>
    <inv:myIdentity>
      <typ:address xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>NAME</typ:name>
        <typ:ico>123</typ:ico>
      </typ:address>
    </inv:myIdentity>
    <inv:intNote>Note</inv:intNote>
  </inv:invoiceHeader>
</inv:invoice>
"""

    result = bytes(etree.tostring(invoice.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_add_items(invoice: Invoice) -> None:

    invoice.add_item({
        'text': 'NAME 1',
        'quantity': 1,
        'rateVAT': 'high',
        'homeCurrency': {
            'unitPrice': 200
        }
    })

    invoice.add_item({
        'quantity': 1,
        'payVAT': 1,
        'rateVAT': 'high',
        'homeCurrency': {
            'unitPrice': 198
        },
        'stockItem': {
            'stockItem': {
                'ids': 'STM'
            }
        }
    })

    expected_xml = b"""<inv:invoice xmlns:inv="http://www.stormware.cz/schema/version_2/invoice.xsd" version="2.0">
  <inv:invoiceHeader>
    <inv:invoiceType>issuedInvoice</inv:invoiceType>
    <inv:date>2015-01-10</inv:date>
    <inv:partnerIdentity>
      <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">25</typ:id>
    </inv:partnerIdentity>
    <inv:myIdentity>
      <typ:address xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>NAME</typ:name>
        <typ:ico>123</typ:ico>
      </typ:address>
    </inv:myIdentity>
    <inv:intNote>Note</inv:intNote>
  </inv:invoiceHeader>
  <inv:invoiceDetail>
    <inv:invoiceItem>
      <inv:text>NAME 1</inv:text>
      <inv:quantity>1</inv:quantity>
      <inv:rateVAT>high</inv:rateVAT>
      <inv:homeCurrency>
        <typ:unitPrice xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">200</typ:unitPrice>
      </inv:homeCurrency>
    </inv:invoiceItem>
    <inv:invoiceItem>
      <inv:quantity>1</inv:quantity>
      <inv:payVAT>1</inv:payVAT>
      <inv:rateVAT>high</inv:rateVAT>
      <inv:homeCurrency>
        <typ:unitPrice xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">198</typ:unitPrice>
      </inv:homeCurrency>
      <inv:stockItem>
        <typ:stockItem xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
          <typ:ids>STM</typ:ids>
        </typ:stockItem>
      </inv:stockItem>
    </inv:invoiceItem>
  </inv:invoiceDetail>
</inv:invoice>
"""

    result = bytes(etree.tostring(invoice.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_add_advance_payment_item(invoice: Invoice) -> None:
    invoice.add_advance_payment_item({
        'sourceDocument': {
            'number': '150800001'
        },
        'quantity': 1,
        'payVAT': False,
        'rateVAT': 'none',
        'homeCurrency': {
            'unitPrice': '-3000',
            'price': '-3000',
            'priceVAT': 0,
            'priceSum': '-3000'
        }
    })

    expected_xml = b"""<inv:invoice xmlns:inv="http://www.stormware.cz/schema/version_2/invoice.xsd" version="2.0">
  <inv:invoiceHeader>
    <inv:invoiceType>issuedInvoice</inv:invoiceType>
    <inv:date>2015-01-10</inv:date>
    <inv:partnerIdentity>
      <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">25</typ:id>
    </inv:partnerIdentity>
    <inv:myIdentity>
      <typ:address xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>NAME</typ:name>
        <typ:ico>123</typ:ico>
      </typ:address>
    </inv:myIdentity>
    <inv:intNote>Note</inv:intNote>
  </inv:invoiceHeader>
  <inv:invoiceDetail>
    <inv:invoiceAdvancePaymentItem>
      <inv:sourceDocument>
        <typ:number xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">150800001</typ:number>
      </inv:sourceDocument>
      <inv:quantity>1</inv:quantity>
      <inv:payVAT>false</inv:payVAT>
      <inv:rateVAT>none</inv:rateVAT>
      <inv:homeCurrency>
        <typ:unitPrice xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">-3000</typ:unitPrice>
        <typ:price xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">-3000</typ:price>
        <typ:priceVAT xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">0</typ:priceVAT>
        <typ:priceSum xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">-3000</typ:priceSum>
      </inv:homeCurrency>
    </inv:invoiceAdvancePaymentItem>
  </inv:invoiceDetail>
</inv:invoice>
"""

    result = bytes(etree.tostring(invoice.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_set_summary(invoice: Invoice) -> None:
    invoice.add_summary({
        'roundingDocument': 'math2one',
        'foreignCurrency': {
            'currency': 'EUR',
            'rate': '20.232',
            'amount': 1,
            'priceSum': 580
        }
    })

    expected_xml = b"""<inv:invoice xmlns:inv="http://www.stormware.cz/schema/version_2/invoice.xsd" version="2.0">
  <inv:invoiceHeader>
    <inv:invoiceType>issuedInvoice</inv:invoiceType>
    <inv:date>2015-01-10</inv:date>
    <inv:partnerIdentity>
      <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">25</typ:id>
    </inv:partnerIdentity>
    <inv:myIdentity>
      <typ:address xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>NAME</typ:name>
        <typ:ico>123</typ:ico>
      </typ:address>
    </inv:myIdentity>
    <inv:intNote>Note</inv:intNote>
  </inv:invoiceHeader>
  <inv:invoiceSummary>
    <inv:roundingDocument>math2one</inv:roundingDocument>
    <inv:foreignCurrency>
      <typ:currency xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:ids>EUR</typ:ids>
      </typ:currency>
      <typ:rate xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">20.232</typ:rate>
      <typ:amount xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">1</typ:amount>
      <typ:priceSum xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">580</typ:priceSum>
    </inv:foreignCurrency>
  </inv:invoiceSummary>
</inv:invoice>
"""

    result = bytes(etree.tostring(invoice.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_set_parameters(invoice: Invoice) -> None:
    invoice.add_parameter('IsOn', 'boolean', 'true')
    invoice.add_parameter('VPrNum', 'number', 10.43)
    invoice.add_parameter('RefVPrCountry', 'list', 'SK', 'Country')
    invoice.add_parameter('CustomList', 'list', {'id': 5}, {'id': 6})

    expected_xml = b"""<inv:invoice xmlns:inv="http://www.stormware.cz/schema/version_2/invoice.xsd" version="2.0">
  <inv:invoiceHeader>
    <inv:invoiceType>issuedInvoice</inv:invoiceType>
    <inv:date>2015-01-10</inv:date>
    <inv:partnerIdentity>
      <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">25</typ:id>
    </inv:partnerIdentity>
    <inv:myIdentity>
      <typ:address xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>NAME</typ:name>
        <typ:ico>123</typ:ico>
      </typ:address>
    </inv:myIdentity>
    <inv:intNote>Note</inv:intNote>
    <inv:parameters>
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
    </inv:parameters>
  </inv:invoiceHeader>
</inv:invoice>
"""

    result = bytes(etree.tostring(invoice.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_can_link_to_order(invoice: Invoice) -> None:
    invoice.add_link({
        'sourceAgenda': 'receivedOrder',
        'sourceDocument': {
            'number': 'number'
        }
    })

    expected_xml = b"""<inv:invoice xmlns:inv="http://www.stormware.cz/schema/version_2/invoice.xsd" version="2.0">
  <inv:links>
    <typ:link xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
      <typ:sourceAgenda>receivedOrder</typ:sourceAgenda>
      <typ:sourceDocument>
        <typ:number>number</typ:number>
      </typ:sourceDocument>
    </typ:link>
  </inv:links>
  <inv:invoiceHeader>
    <inv:invoiceType>issuedInvoice</inv:invoiceType>
    <inv:date>2015-01-10</inv:date>
    <inv:partnerIdentity>
      <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">25</typ:id>
    </inv:partnerIdentity>
    <inv:myIdentity>
      <typ:address xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>NAME</typ:name>
        <typ:ico>123</typ:ico>
      </typ:address>
    </inv:myIdentity>
    <inv:intNote>Note</inv:intNote>
  </inv:invoiceHeader>
</inv:invoice>
"""

    result = bytes(etree.tostring(invoice.get_xml(), pretty_print=True))
    assert result == expected_xml
