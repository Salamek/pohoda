# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.offer.Header import Header
from pohoda.entity.offer.Item import Item
from pohoda.entity.offer.Summary import Summary


class Offer(Agenda, AddParameterToHeaderTrait):
    import_root = 'lst:offer'

    def __init__(self, data: dict, ico: str):
        if data:
            data = {'header': Header(data, ico)}

        super().__init__(data, ico)

    def add_item(self, data: dict) -> 'Offer':
        """
        Add order item.
        :param data:
        :return:
        """

        if not self._data.get('offerDetail'):
            self._data['offerDetail'] = []

        self._data['offerDetail'].append(Item(data, self._ico))
        return self

    def add_summary(self, data: dict) -> 'Offer':
        """
        Add order summary.
        :param data:
        :return:
        """

        self._data['summary'] = Summary(data, self._ico)
        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('offer', namespace='ofr')
        xml.set('version', '2.0')
        self._add_elements(xml, ['header', 'offerDetail', 'summary'], 'ofr')
        return xml
