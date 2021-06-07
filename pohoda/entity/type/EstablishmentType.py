# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class EstablishmentType(Agenda):
    _elements = ['company', 'city', 'street', 'zip']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('establishment', namespace='typ')
        self._add_elements(xml, self._elements, 'typ')
        return xml
