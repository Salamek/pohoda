# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.list_request.Filter import Filter
from pohoda.entity.list_request.UserFilterName import UserFilterName


class ListRequest(Agenda):

    def add_filter(self, data: dict) -> 'ListRequest':
        """
        Add filter.
        :param data:
        :return:
        """

        self._data['filter'] = Filter(data, self._ico)
        return self

    def add_user_filter_name(self, name: str) -> 'ListRequest':
        """
        Add user filter name.
        :param name:
        :return:
        """

        self._data['userFilterName'] = UserFilterName({'userFilterName': name}, self._ico)
        return self

    def get_xml(self) -> etree.Element:

        xml = self._create_xml_tag(
            'list{}Request'.format(self._data['type']),
            namespace=self._data['namespace']
        )
        xml.set('version', '2.0')

        # IntParam doesn't have the version attribute
        if self._data['type'] != 'IntParam':
            xml.set(self._get_lc_first_type() + 'Version', '2.0')

        first_type = self._data.get(self._get_lc_first_type() + 'Type')
        if first_type:
            xml.set(self._get_lc_first_type() + 'Type', first_type)

        request = self._create_xml_tag('request{}'.format(self._data['type']), namespace=self._data['namespace'])
        xml.append(request)
        self._add_elements(request, ['filter', 'userFilterName'], 'ftr')
        return xml

    def _get_lc_first_type(self) -> str:
        """
        Get LC first type name.
        :return:
        """

        # ActionPrice is custom
        if self._data['type'] == 'ActionPrice':
            return 'actionPrices'

        modify_str = self._data['type']
        return modify_str[0].lower() + modify_str[1:]
