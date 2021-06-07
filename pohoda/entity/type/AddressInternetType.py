# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class AddressInternetType(Agenda):
    _elements = ['company', 'title', 'surname', 'name', 'city', 'street', 'number', 'zip', 'ico', 'dic', 'icDph',
                 'phone', 'mobilPhone', 'fax', 'email', 'www']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('address', namespace='typ')
        self._add_elements(xml, self._elements, 'typ')
        return xml
