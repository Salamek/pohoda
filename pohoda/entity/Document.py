from typing import List
from importlib import import_module
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.document.Part import Part
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait


class Document(Agenda, AddParameterToHeaderTrait):

    def __init__(self, data: dict, ico: str):
        self._ico = ico

        if data:
            data = {
                'header': self._get_document_part('Header', data, ico)
            }

        self._data = data

        super().__init__(data, ico)

    def _get_document_name(self) -> str:
        raise NotImplementedError

    def _get_document_namespace(self) -> str:
        raise NotImplementedError

    def _get_document_elements(self) -> List[str]:
        return ['header', '{}Detail'.format(self._get_document_name()), 'summary']

    def _get_document_part(self, name: str, data: dict, ico: str) -> Part:
        part_name = 'pohoda.entity.{}.{}'.format(self.__class__.__name__.lower(), name)

        try:
            entity = getattr(import_module(part_name), name)
            if not issubclass(entity, Part):
                raise ValueError('Not allowed entity: {}'.format(name))
            part = entity(data, ico)
            part.set_namespace(self._get_document_namespace())
            part.set_node_prefix(self._get_document_name())
            return part
        except ImportError as e:
            raise ValueError('Entity {} not found'.format(name)) from e

    def add_item(self, data: dict) -> 'Document':
        key = '{}Detail'.format(self._get_document_name())
        if key not in self._data:
            self._data[key] = []

        self._data[key].append(self._get_document_part('Item', data, self._ico))

        return self

    def add_summary(self, data: dict) -> 'Document':
        self._data['summary'] = self._get_document_part('Summary', data, self._ico)

        return self

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag(self._get_document_name(), namespace=self._get_document_namespace())
        xml.set('version', '2.0')
        self._add_elements(xml, self._get_document_elements(), self._get_document_namespace())
        return xml
