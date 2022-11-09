from lxml import etree
from pohoda.entity.document.Part import Part
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.type.Address import Address
from pohoda.entity.type.MyAddress import MyAddress


class Header(Part, AddParameterTrait):

    def __init__(self, data: dict, ico: str):
        partner_identity = data.get('partnerIdentity')
        if partner_identity:
            data['partnerIdentity'] = Address(partner_identity, ico)

        # process my identity
        my_identity = data.get('myIdentity')
        if my_identity:
            data['myIdentity'] = MyAddress(my_identity, ico)

        super().__init__(data, ico)

    def get_xml(self) -> etree.Element:

        if not self._namespace:
            raise ValueError('Namespace not set.')

        if not self._node_prefix:
            raise ValueError('Node name prefix not set.')

        xml = self._create_xml_tag('{}Header'.format(self._node_prefix), namespace=self._namespace)
        self._add_elements(xml, self._elements + ['parameters'], self._namespace)
        return xml
