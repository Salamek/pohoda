# coding: utf-8

from pohoda.entity.Agenda import Agenda


class ActionPrice(Agenda):
    import_root = 'lst:actionPrice'

    def get_xml(self):
        raise NotImplementedError('Action prices import is currently not supported.')
