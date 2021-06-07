# coding: utf-8

from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.addressbook.Header import Header
from pohoda.entity.common.AddActionTypeTrait import AddActionTypeTrait
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait


class Addressbook(Agenda, AddActionTypeTrait, AddParameterToHeaderTrait):
    import_root = 'lAdb:addressbook'

    def __init__(self, data: dict, ico: str):
        if data:
            data = {
                'header': Header(data, ico)
            }
        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('addressbook', namespace='adb')
        xml.set('version', '2.0')
        self._add_elements(xml, ['actionType', 'header'], 'adb')
        return xml
