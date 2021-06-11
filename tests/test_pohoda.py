import pytest
import tempfile
import os
from lxml import etree
from pohoda.Pohoda import Pohoda
from pohoda.entity.Stock import Stock


@pytest.fixture(scope="function")  # type: ignore
def pohoda() -> Pohoda:
    return Pohoda('123', 'ABC')


def test_be_constructed_with() -> None:
    Pohoda('123', 'ABC')


def test_throws_exception_on_wrong_agenda_name(pohoda: Pohoda) -> None:
    with pytest.raises(ValueError):
        pohoda.createBullshit()


def test_creates_existing_objects(pohoda: Pohoda) -> None:
    created = pohoda.create('Stock', {
        'code': 'CODE',
        'name': 'NAME',
        'storage': 'STORAGE',
        'typePrice': {'id': 1}
    })

    assert isinstance(created, Stock)


def test_can_write_file(pohoda: Pohoda) -> None:

    stock = Stock({
        'code': 'CODE',
        'name': 'NAME',
        'storage': 'STORAGE',
        'typePrice': {'id': 1}
    }, '123')

    pohoda.add_item('ITEM_ID', stock)

    temp_file = os.path.join(tempfile.gettempdir(), 'pohoda.xml')
    pohoda.write(temp_file)

    with open(temp_file, 'rb') as f:
        xml_content = f.read()
        parsed_xml = etree.fromstring(xml_content)
        assert parsed_xml.get('id') == 'ABC'
        assert parsed_xml.get('ico') == '123'
        assert parsed_xml.get('note') is None

        # test data_pack_item properties
        assert parsed_xml.xpath('//dat:dataPack/dat:dataPackItem/@id', namespaces={
            'dat': 'http://www.stormware.cz/schema/version_2/data.xsd'
        }) == ['ITEM_ID']

    os.unlink(temp_file)
