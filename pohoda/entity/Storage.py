# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class Storage(Agenda):
    import_root = 'lst:itemStorage'

    def add_substorage(self, storage: 'Storage') -> None:
        """
        Add substorage.
        :param storage:
        :return:
        """

        if not self._data.get('subStorages'):
            self._data['subStorages'] = []

        self._data['subStorages'].append(storage)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('storage', namespace='str')
        xml.set('version', '2.0')
        self.storage_xml(xml)
        return xml

    def storage_xml(self, xml: etree.Element) -> None:
        """
        Attach storage to XML element.
        :param xml:
        :return:
        """

        storage = self._create_xml_tag('itemStorage', namespace='str')
        storage.set('code', self._data['code'])
        xml.append(storage)

        if self._data.get('name'):
            storage.set('name', self._data['name'])

        sub_storages = self._data.get('subStorages')
        if sub_storages:
            sub_storages_element = self._create_xml_tag('subStorages', namespace='str')
            storage.append(sub_storages_element)
            for sub_storage in sub_storages:
                sub_storage.storage_xml(sub_storages_element)
