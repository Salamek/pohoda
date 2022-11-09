import pytest
import datetime
from lxml import etree

from pohoda.entity.Agenda import Agenda
from pohoda.entity.ListRequest import ListRequest


@pytest.fixture(scope="function")  # type: ignore
def list_request() -> ListRequest:
    return ListRequest({
        'type': 'ActionPrice'
    }, '123')


def test_be_constructed_with() -> None:
    ListRequest({
        'type': 'ActionPrice'
    }, '123')


def test_extends_agenda(list_request: ListRequest) -> None:
    assert isinstance(list_request, Agenda)


def test_creates_correct_xml_for_category() -> None:
    expected_xml = b"""<lst:listCategoryRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="2.0" categoryVersion="2.0">
  <lst:requestCategory/>
</lst:listCategoryRequest>
"""
    list_request = ListRequest({
        'type': 'Category'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_action_prices() -> None:
    expected_xml = b"""<lst:listActionPriceRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="2.0" actionPricesVersion="2.0">
  <lst:requestActionPrice/>
</lst:listActionPriceRequest>
"""
    list_request = ListRequest({
        'type': 'ActionPrice'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_order() -> None:
    expected_xml = b"""<lst:listOrderRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="2.0" orderVersion="2.0" orderType="receivedOrder">
  <lst:requestOrder/>
</lst:listOrderRequest>
"""
    list_request = ListRequest({
        'type': 'Order'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_advance_invoice() -> None:
    expected_xml = b"""<lst:listInvoiceRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="2.0" invoiceVersion="2.0" invoiceType="issuedAdvanceInvoice">
  <lst:requestInvoice/>
</lst:listInvoiceRequest>
"""
    list_request = ListRequest({
        'type': 'Invoice',
        'invoiceType': 'issuedAdvanceInvoice'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_vydejka() -> None:
    expected_xml = b"""<lst:listVydejkaRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="2.0" vydejkaVersion="2.0">
  <lst:requestVydejka/>
</lst:listVydejkaRequest>
"""
    list_request = ListRequest({
        'type': 'Vydejka'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_issue_slip() -> None:
    expected_xml = b"""<lst:listVydejkaRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="2.0" vydejkaVersion="2.0">
  <lst:requestVydejka/>
</lst:listVydejkaRequest>
"""
    list_request = ListRequest({
        'type': 'IssueSlip'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_address_book() -> None:
    expected_xml = b"""<lAdb:listAddressBookRequest xmlns:lAdb="http://www.stormware.cz/schema/version_2/list_addBook.xsd" version="2.0" addressBookVersion="2.0">
  <lAdb:requestAddressBook/>
</lAdb:listAddressBookRequest>
"""
    list_request = ListRequest({
        'type': 'Addressbook'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_int_params() -> None:
    expected_xml = b"""<lst:listIntParamRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="2.0">
  <lst:requestIntParam/>
</lst:listIntParamRequest>
"""
    list_request = ListRequest({
        'type': 'IntParam'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_user_lists() -> None:
    expected_xml = b"""<lst:listUserCodeRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="1.1" listVersion="1.1"/>
"""
    list_request = ListRequest({
        'type': 'UserList'
    }, '123')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_invoice_with_user_filter_name() -> None:
    expected_xml = b"""<lst:listInvoiceRequest xmlns:lst="http://www.stormware.cz/schema/version_2/list.xsd" version="2.0" invoiceVersion="2.0" invoiceType="issuedInvoice">
  <lst:requestInvoice>
    <ftr:userFilterName xmlns:ftr="http://www.stormware.cz/schema/version_2/filter.xsd">CustomFilter</ftr:userFilterName>
  </lst:requestInvoice>
</lst:listInvoiceRequest>
"""
    list_request = ListRequest({
        'type': 'Invoice'
    }, '123')

    list_request.add_user_filter_name('CustomFilter')

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml


def test_creates_correct_xml_for_stock_with_complex_filter() -> None:
    expected_xml = b"""<lStk:listStockRequest xmlns:lStk="http://www.stormware.cz/schema/version_2/list_stock.xsd" version="2.0" stockVersion="2.0">
  <lStk:requestStock>
    <ftr:filter xmlns:ftr="http://www.stormware.cz/schema/version_2/filter.xsd">
      <ftr:storage>
        <typ:ids xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">MAIN</typ:ids>
      </ftr:storage>
      <ftr:lastChanges>2018-04-29T14:30:00</ftr:lastChanges>
    </ftr:filter>
  </lStk:requestStock>
</lStk:listStockRequest>
"""
    list_request = ListRequest({
        'type': 'Stock'
    }, '123')

    list_request.add_filter({
        'storage': {
            'ids': 'MAIN'
        },
        'lastChanges': datetime.datetime(
            year=2018,
            month=4,
            day=29,
            hour=14,
            minute=30,
            second=0
        ),
    })

    result = bytes(etree.tostring(list_request.get_xml(), pretty_print=True))
    assert result == expected_xml
