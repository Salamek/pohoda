# coding: utf-8

from pohoda.entity.Agenda import Agenda


class IndividualPrice(Agenda):
    import_root = 'lst:individualPrice'

    def get_xml(self):
        raise NotImplementedError('Individual prices import is currently not supported.')
