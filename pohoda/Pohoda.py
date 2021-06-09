import re
from typing import Any, Optional
from importlib import import_module

from lxml import etree

from pohoda.entity.Agenda import Agenda


class Pohoda:
    encoding = 'windows-1250'
    _ico = None
    _application = 'Python Pohoda connector'

    _xml_root = None
    _filename = None

    def __init__(self, ico: str, id_: Optional[str] = None, note: Optional[str] = None):
        self._ico = ico

        # Register namespaces
        for namespace_key, namespace_value in Agenda.namespaces.items():
            etree.register_namespace(namespace_key, namespace_value)

        self.initialize_xml_root(id_, note)

    def set_application_name(self, name: str) -> None:
        """
        Set the name of the application.
        :param name:
        :return:
        """
        self._application = name

    def create(self, name: str, data: Optional[dict] = None) -> Agenda:
        """
        Create and return instance of requested agenda.
        :param name:
        :param data:
        :return: Agenda
        """
        if data is None:
            data = {}

        try:
            entity = getattr(import_module('pohoda.entity.{}'.format(name)), name)
            if not issubclass(entity, Agenda):
                raise ValueError('Not allowed entity: {}'.format(name))
            return entity(data, self._ico)
        except ImportError as e:
            raise ValueError('Entity {} not found'.format(name)) from e

    def initialize_xml_root(self, id_: Optional[str] = None, note: Optional[str] = None) -> None:
        """
        Open new XML file for writing.
        :param id_:
        :param note:
        :return:
        """
        self._xml_root = etree.Element(Agenda.with_xml_namespace('dat', 'dataPack'))
        self._xml_root.set('ico', self._ico)
        self._xml_root.set('application', self._application)
        self._xml_root.set('version', '2.0')

        if note:
            self._xml_root.set('note', note)

        if id_:
            self._xml_root.set('id', id_)

    def add_item(self, id_: str, agenda: Agenda) -> None:
        """
        Add item.
        :param id_:
        :param agenda:
        :return:
        """
        data_pack_item = etree.SubElement(self._xml_root, Agenda.with_xml_namespace('dat', 'dataPackItem'))
        data_pack_item.set('id', id_)
        data_pack_item.set('version', '2.0')
        data_pack_item.append(agenda.get_xml())

    def write(self, filename: str, pretty_print: bool = True) -> None:
        """
        Write xml tree to file
        :param filename:
        :param pretty_print:
        :return:
        """

        tree = etree.ElementTree(self._xml_root)
        tree.write(filename, xml_declaration=True, encoding=self.encoding, method='xml', pretty_print=pretty_print)

    def load(self, name: str, filename: str) -> None:
        raise NotImplementedError

    def next(self) -> None:
        raise NotImplementedError

    def __getattr__(self, name: str) -> Any:
        """
        Handle dynamic method calls.
        :param name:
        :return:
        """

        def _getattr_resolver(*args: Any) -> Any:
            match_create = re.match(r'^create_([a-zA-Z0-9]*)$', name)
            if match_create:
                return getattr(self, 'create')(match_create.group(1).capitalize(), args[0])

            match_load = re.match(r'^load_([a-zA-Z0-9]*)$', name)
            if match_load:
                if not args[0]:
                    raise ValueError('Filename is not set')
                return getattr(self, 'create')(match_load.group(1).capitalize(), args[0])

            raise ValueError('Unknown method: {}'.format(name))

        return _getattr_resolver
