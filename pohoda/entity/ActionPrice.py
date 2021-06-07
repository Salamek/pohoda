# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class ActionPrice(Agenda):
    import_root = 'lst:actionPrice'

    def get_xml(self) -> etree.Element:
        raise NotImplementedError('Action prices import is currently not supported.')
