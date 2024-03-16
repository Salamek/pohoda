from lxml import etree
from pohoda.entity.Agenda import Agenda


class StatementNumber(Agenda):
    _elements = ['statementNumber', 'numberMovement']

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('statementNumber', namespace='bnk')
        self._add_elements(xml, self._elements, 'bnk')
        return xml
