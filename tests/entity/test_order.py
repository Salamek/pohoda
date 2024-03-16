import pytest
import datetime
from lxml import etree

from pohoda.entity.Agenda import Agenda
from pohoda.entity.Order import Order


default_header = b"""
    <ord:orderType>receivedOrder</ord:orderType>
    <ord:date>2015-01-10</ord:date>
    <ord:partnerIdentity>
      <typ:id xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">25</typ:id>
    </ord:partnerIdentity>
    <ord:myIdentity>
      <typ:address xmlns:typ="http://www.stormware.cz/schema/version_2/type.xsd">
        <typ:name>NAME</typ:name>
        <typ:ico>123</typ:ico>
      </typ:address>
    </ord:myIdentity>
    <ord:intNote>Note</ord:intNote>
  """


@pytest.fixture(scope="function")  # type: ignore
def order() -> Order:
    return Order({
        'partnerIdentity': {
            'id': 25
        },
        'myIdentity': {
            'address': {
                'name': 'NAME',
                'ico': '123'
            }
        },
        'date': '2015-01-10',
        'intNote': 'Note'
    }, '123')


def test_be_constructed_with() -> None:
    Order({
        'partnerIdentity': {
            'id': 25
        },
        'myIdentity': {
            'address': {
                'name': 'NAME',
                'ico': '123'
            }
        },
        'date': '2015-01-10',
        'intNote': 'Note'
    }, '123')


def test_extends_agenda(order: Order) -> None:
    assert isinstance(order, Order)
    assert isinstance(order, Agenda)


def test_creates_correct_xml(order: Order) -> None:
    expected_xml = b"""<ord:order xmlns:ord="http://www.stormware.cz/schema/version_2/order.xsd" version="2.0">
  <ord:orderHeader>""" + default_header + b"""</ord:orderHeader>
</ord:order>
"""

    result = bytes(etree.tostring(order.get_xml(), pretty_print=True))
    assert result == expected_xml
