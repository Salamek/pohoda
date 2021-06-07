# coding: utf-8

from typing import Optional
from pohoda.entity.type.ActionType import ActionType
from pohoda.entity.common.Trait import Trait


class AddActionTypeTrait(Trait):

    def add_action_type(self,
                        type_: Optional[str] = None,
                        filter_: Optional[str] = None,
                        agenda: Optional[str] = None
                        ) -> 'AddActionTypeTrait':
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
