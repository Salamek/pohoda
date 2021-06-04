import html

from lxml import etree


class Agenda:
    namespaces = {
        'adb': 'http://www.stormware.cz/schema/version_2/addressbook.xsd',
        'con': 'http://www.stormware.cz/schema/version_2/contract.xsd',
        'ctg': 'http://www.stormware.cz/schema/version_2/category.xsd',
        'dat': 'http://www.stormware.cz/schema/version_2/data.xsd',
        'ftr': 'http://www.stormware.cz/schema/version_2/filter.xsd',
        'int': 'http://www.stormware.cz/schema/version_2/intDoc.xsd',
        'inv': 'http://www.stormware.cz/schema/version_2/invoice.xsd',
        'ipm': 'http://www.stormware.cz/schema/version_2/intParam.xsd',
        'lAdb': 'http://www.stormware.cz/schema/version_2/list_addBook.xsd',
        'lst': 'http://www.stormware.cz/schema/version_2/list.xsd',
        'lStk': 'http://www.stormware.cz/schema/version_2/list_stock.xsd',
        'ord': 'http://www.stormware.cz/schema/version_2/order.xsd',
        'pre': 'http://www.stormware.cz/schema/version_2/prevodka.xsd',
        'pri': 'http://www.stormware.cz/schema/version_2/prijemka.xsd',
        'prn': 'http://www.stormware.cz/schema/version_2/print.xsd',
        'pro': 'http://www.stormware.cz/schema/version_2/prodejka.xsd',
        'str': 'http://www.stormware.cz/schema/version_2/storage.xsd',
        'stk': 'http://www.stormware.cz/schema/version_2/stock.xsd',
        'typ': 'http://www.stormware.cz/schema/version_2/type.xsd',
        'vyd': 'http://www.stormware.cz/schema/version_2/vydejka.xsd'
    }

    _ico = None

    _data = {}

    _ref_elements = []

    _elements_attributes_mapper = {}
    _resolvers = []

    def __init__(self, data: dict = None, ico: str = None):
        """
        Construct agenda using provided data.
        :param data:
        :param ico:
        """

        self._ico = ico
        self._data = data

    def get_xml(self):
        """
        Get XML.
        :return:
        """
        pass

    def _create_xml_tag(self, tag: str, namespace: str = None):
        """
        Create XML.
        :return:
        """

        return etree.Element(self.with_xml_namespace(namespace, tag)) if namespace else etree.Element(tag)

    def _resolve_namespace(self, short: str = None) -> str:
        """
        Get namespace.
        :param short:
        :return:
        """

        found_namespace = self.namespaces.get(short)
        if not found_namespace:
            ValueError('Unknown namespace key {}'.format(short))
        return found_namespace

    @staticmethod
    def with_xml_namespace(namespace_key: str, tag_name: str):
        found_namespace = Agenda.namespaces.get(namespace_key)
        if not found_namespace:
            ValueError('Unknown namespace key {}'.format(namespace_key))
        return '{{{}}}{}'.format(found_namespace, tag_name)

    def _add_elements(self, xml, elements: list, namespace: str = None):
        """
        Add batch elements.
        :param xml:
        :param elements:
        :param namespace:
        :return:
        """
        for element in elements:
            found_element_in_data = self._data.get(element)
            if not found_element_in_data:
                continue

            # is ref element
            if element in self._ref_elements:
                self._add_ref_element(xml, element, found_element_in_data, namespace)
                continue

            found_element_attributes_mapper = self._elements_attributes_mapper.get(element)
            if found_element_attributes_mapper:
                attr_element, attr_name, attr_namespace = found_element_attributes_mapper

                # get element
                attr_element = xml.findall(
                    self.with_xml_namespace(namespace, attr_element) if namespace else attr_element)
                if attr_element:
                    attr_element.set(
                        self.with_xml_namespace(attr_namespace, attr_name) if attr_namespace else attr_name,
                        html.escape(found_element_in_data))

                continue

            # Agenda object
            if isinstance(found_element_in_data, Agenda):

                # set namespace
                if namespace and hasattr(found_element_in_data, 'set_namespace'):
                    found_element_in_data.set_namespace(namespace)

                # set node name
                if hasattr(found_element_in_data, 'set_node_name'):
                    found_element_in_data.set_node_name(element)

                self._append_node(xml, found_element_in_data.get_xml())
                continue

            # list of Agenda objects
            if isinstance(found_element_in_data, list):
                child = etree.Element(self.with_xml_namespace(namespace, element) if namespace else element)
                for node in found_element_in_data:
                    self._append_node(child, node.get_xml())
                xml.append(child)
                continue

            child = etree.Element(self.with_xml_namespace(namespace, element) if namespace else element)

            # !FIXME resolve datetime better then just cast to str
            child.text = html.escape(str(found_element_in_data))
            xml.append(child)

    def _add_ref_element(self, xml, name: str, value, namespace: str = None):
        """
        Add ref element.
        :param xml:
        :param name:
        :param value:
        :param namespace:
        :return:
        """

        node = etree.Element(self.with_xml_namespace(namespace, name) if namespace else name)

        if not isinstance(value, list):
            value = {'ids': value}

        for k, v in value.items():
            node_child = etree.Element(self.with_xml_namespace('typ', k))
            node_child.text = html.escape(str(v))
            node.append(node_child)

        return node

    def _append_node(self, xml, node):
        """
        Append node to another node.
        :param xml:
        :param node:
        :return:
        """
        xml.append(node)
