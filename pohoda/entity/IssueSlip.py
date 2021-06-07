# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.issue_slip.Header import Header
from pohoda.entity.issue_slip.Item import Item
from pohoda.entity.issue_slip.Summary import Summary


class IssueSlip(Agenda, AddParameterToHeaderTrait):
    import_root = 'lst:vydejka'

    def __init__(self, data: dict, ico: str):
        data = {'header': Header(data, ico)}
        super().__init__(data, ico)

    def add_item(self, data: dict) -> 'IssueSlip':
        """
        Add item.
        :param data:
        :return:
        """

        if not self._data.get('vydejkaDetail'):
            self._data['vydejkaDetail'] = []

        self._data['vydejkaDetail'].append(Item(data, self._ico))
        return self

    def add_summary(self, data: dict) -> 'IssueSlip':
        """
        Add summary.
        :param data:
        :return:
        """

        self._data['summary'] = Summary(data, self._ico)
        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('vydejka', namespace='vyd')
        xml.set('version', '2.0')
        self._add_elements(xml, ['header', 'vydejkaDetail', 'summary'], 'vyd')
        return xml
