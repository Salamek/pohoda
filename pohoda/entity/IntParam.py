# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.int_param.Settings import Settings


class IntParam(Agenda):
    import_root = 'lst:intParamDetail'
    _elements = ['name', 'description', 'parameterType', 'parameterSettings']

    def __init__(self, data: dict, ico: str):
        # prepare empty parameter list for list
        if data['parameterType'] == 'listValue':
            data['parameterSettings'] = {'parameterList': []}

        # process settings
        parameter_settings = data.get('parameterSettings')
        if parameter_settings:
            data['parameterSettings'] = Settings(parameter_settings, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('intParamDetail', namespace='ipm')
        xml.set('version', '2.0')
        param = xml.addchild('ipm:intParam')
        self._add_elements(param, self._elements, 'ipm')
        return xml
