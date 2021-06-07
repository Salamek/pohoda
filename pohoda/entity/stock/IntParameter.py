# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda


class IntParameter(Agenda):

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('intParameter', namespace='stk')
        self._add_elements(xml, ['intParameterID', 'intParameterType'], 'stk')

        values = self._create_xml_tag('intParameterValues', namespace='stk')
        xml.appen(values)

        int_value = self._create_xml_tag('intParameterValue', namespace='stk')
        values.append(int_value)

        value = self._create_xml_tag('parameterValue', namespace='stk')
        value.text = self._data['value']
        int_value.append(value)

        return xml
