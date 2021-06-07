# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.user_list.ItemUserCode import ItemUserCode


class UserList(Agenda):
    import_root = 'lst:listUserCode'

    def add_item_user_code(self, data: dict) -> None:
        """
        Add item user code.
        :param data:
        :return:
        """

        if not self._data.get('itemUserCodes'):
            self._data['itemUserCodes'] = []

        self._data['itemUserCodes'].append(ItemUserCode(data, self._ico))

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('listUserCode', namespace='lst')
        xml.set('version', '1.1')
        xml.set('code', self._data['code'])
        xml.set('name', self._data['name'])

        constants = self._data.get('constants', 'false')
        if constants == 'true':
            xml.set('constants', constants)

        item_user_codes = self._data.get('itemUserCodes')
        if item_user_codes:
            for item_user_code in item_user_codes:
                xml.append(item_user_code.get_xml())

        return xml
