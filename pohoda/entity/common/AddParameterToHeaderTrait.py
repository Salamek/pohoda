# coding: utf-8
from typing import Any
from pohoda.entity.common.Trait import Trait


class AddParameterToHeaderTrait(Trait):
    def add_parameter(self,
                      name: str,
                      parameter_type: str,
                      value: Any,
                      list_: Any = None) -> 'AddParameterToHeaderTrait':
        """
        Set user-defined parameter.
        :param name: (can be set without preceding VPr / RefVPr)
        :param parameter_type:
        :param value:
        :param list_:
        :return:
        """

        self._data['header'].add_parameter(name, parameter_type, value, list_)
        return self
