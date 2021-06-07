# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.print_request.Pdf import Pdf
from pohoda.entity.print_request.Report import Report


class PrinterSettings(Agenda):
    _elements = ['report', 'printer', 'pdf']

    def __init__(self, data: dict, ico: str):
        # process report
        report = data.get('report')
        if report:
            data['report'] = Report(report, ico)

        # process pdf
        pdf = data.get('pdf')
        if pdf:
            data['pdf'] = Pdf(pdf, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('printerSettings', namespace='prn')
        self._add_elements(xml, self._elements, 'prn')
        return xml
