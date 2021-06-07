# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.print_request.PrinterSettings import PrinterSettings
from pohoda.entity.print_request.Record import Record


class PrintRequest(Agenda):

    def __init__(self, data: dict, ico: str):
        # process record
        data['record'] = Record(data['record'], ico, )
        # process printer settings
        data['printerSettings'] = PrinterSettings(data['printerSettings'], ico)
        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('print', namespace='prn')
        xml.set('version', '1.0')
        self._add_elements(xml, ['record', 'printerSettings'], 'prn')
        return xml
