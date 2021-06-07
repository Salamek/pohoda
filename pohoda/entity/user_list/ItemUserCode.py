# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class ItemUserCode(Agenda):

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('itemUserCode', namespace='lst')
        xml.set('code', self._data['code'])
        xml.set('name', self._data['name'])
        if self._data.get('constants'):
            xml.set('constants', self._data['constants'])

        return xml
