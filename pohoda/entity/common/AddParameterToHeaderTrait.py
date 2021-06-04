# coding: utf-8
class AddParameterToHeaderTrait:
    def add_parameter(self, name: str, parameter_type: str, value, list_=None):
        """
        Set user-defined parameter.
        :param name: (can be set without preceding VPr / RefVPr)
        :param parameter_type:
        :param value:
        :param list_:
        :return:
        """

        self._data['header'].addparameter(name, parameter_type, value, list_)
        return self
