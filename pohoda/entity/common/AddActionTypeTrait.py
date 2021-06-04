# coding: utf-8

from pohoda.entity.type.ActionType import ActionType


class AddActionTypeTrait:

    def add_action_type(self, type_: str = None, filter_: str = None, agenda: str = None):
        """
        Add action type.
        :param type_:
        :param filter_:
        :param agenda:
        :return:
        """

        action_type = self._data.get('actionType')
        if action_type:
            raise ValueError('Duplicate action type.')

        self._data['actionType'] = ActionType({'type': type_, 'filter': filter_, 'agenda': agenda}, self._ico)
        return self
