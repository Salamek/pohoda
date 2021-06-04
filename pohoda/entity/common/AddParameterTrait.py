# coding: utf-8

from pohoda.entity.type.Parameter import Parameter


class AddParameterTrait:

    def add_parameter(self, name: str, parameter_type: str, value, list_=None):
        """
        Set user-defined parameter.
        :param name: (can be set without preceding VPr / RefVPr)
        :param parameter_type:
        :param value:
        :param list_:
        :return:
        """

        if not self._data.get('parameters'):
            self._data['parameters'] = []

        self._data['parameters'].append(Parameter({
            'name': name,
            'type': parameter_type,
            'value': value,
            'list': list_
        }, self._ico))

        return self
