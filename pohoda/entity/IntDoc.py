# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.int_doc.Header import Header
from pohoda.entity.int_doc.Item import Item
from pohoda.entity.int_doc.Summary import Summary


class IntDoc(Agenda, AddParameterToHeaderTrait):
    import_root = 'lst:intDoc'

    def __init__(self, data: dict, ico: str):
        data = {
            'header': Header(data, ico)
        }
        super().__init__(data, ico)

    def add_item(self, data: dict) -> 'IntDoc':
        """
        Add intDoc item.
        :param data:
        :return:
        """

        if not self._data.get('intDocDetail'):
            self._data['intDocDetail'] = []

        self._data['intDocDetail'].append(Item(data, self._ico))
        return self

    def add_summary(self, data: dict) -> 'IntDoc':
        """
        Add intDoc summary.
        :param data:
        :return:
        """

        self._data['summary'] = Summary(data, self._ico)
        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('intDoc', namespace='int')
        xml.set('version', '2.0')
        self._add_elements(xml, ['header', 'intDocDetail', 'summary'], 'int')
        return xml
