# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.SetNamespaceTrait import SetNamespaceTrait


class ActionType(Agenda, SetNamespaceTrait):
    def get_xml(self) -> etree.Element:

        if not self._namespace:
            raise ValueError('Namespace not set.')
        # end if
        xml = self._create_xml_tag('actionType', namespace=self._namespace)
        action = self._create_xml_tag('add' if self._data['type'] == 'add/update' else self._data['type'],
                                      namespace=self._namespace)
        xml.append(action)
        if self._data['type'] == 'add/update':
            action.set('update', 'true')

        if self._data['filter']:
            filter_ = self._create_xml_tag('filter', namespace='ftr')
            action.append(filter_)
            if self._data['agenda']:
                filter_.set('agenda', self._data['agenda'])

            for property_, value_ in self._data['filter'].items():
                ftr = self._create_xml_tag(property_, namespace='ftr')
                ftr.text = None if isinstance(value_, dict) else value_
                if isinstance(value_, dict):
                    for t_property, t_value in value_.items():
                        ftr_child = self._create_xml_tag(t_property, namespace='typ')
                        ftr_child.text = t_value
                        ftr.append(ftr_child)
        return xml
