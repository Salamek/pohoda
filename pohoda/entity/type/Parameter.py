# coding: utf-8
import html
from lxml import etree
from pohoda.entity.Agenda import Agenda


class Parameter(Agenda):
    _namespace = None

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('parameter', namespace='typ')
        child = self._create_xml_tag('name', namespace='typ')
        child.text = self._data['name']
        xml.append(child)

        if self._data['type'] == 'list':
            self._add_ref_element(xml, 'listValueRef', self._data['value'], namespace='typ')
            if self._data['list']:
                self._add_ref_element(xml, 'list', self._data['list'], namespace='typ')
            return xml

        not_list_child = self._create_xml_tag(self._data['type'] + 'Value', namespace='typ')
        not_list_child.text = html.escape(str(self._data['value']))
        xml.append(not_list_child)
        return xml
