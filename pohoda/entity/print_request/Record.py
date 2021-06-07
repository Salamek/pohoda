# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.print_request.Filter import Filter


class Record(Agenda):
    def __init__(self, data: dict, ico: str):
        # process filter
        filter_ = data.get('filter')
        if filter_:
            data['filter'] = Filter(filter_, ico)
        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('record', 'prn')
        xml.set('agenda', self._data['agenda'])
        self._add_elements(xml, ['filter'], 'prn')
        return xml
