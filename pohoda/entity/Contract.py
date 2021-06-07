# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.contract.Desc import Desc


class Contract(Agenda, AddParameterToHeaderTrait):
    import_root = 'lCon:contract'

    def __init__(self, data: dict, ico: str):
        data = {
            'header': Desc(data, ico)
        }
        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('contract', namespace='con')
        xml.set('version', '2.0')
        self._add_elements(xml, ['header'], 'con')
        return xml
