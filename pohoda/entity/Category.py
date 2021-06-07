# coding: utf-8
from lxml import etree
from pohoda.entity.Agenda import Agenda


class Category(Agenda):
    import_root = 'ctg:category'

    _elements = ['name', 'description', 'sequence', 'displayed', 'picture', 'note']

    def add_subcategory(self, category: 'Category') -> None:
        """
        Add subcategory.
        :param category:
        :return:
        """

        if not self._data.get('subCategories'):
            self._data['subCategories'] = []

        self._data['subCategories'].append(category)

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('categoryDetail', namespace='ctg')
        xml.set('version', '2.0')
        self.category_xml(xml)
        return xml

    def category_xml(self, xml: etree.Element) -> None:
        """
        Attach category to XML element.
        :param xml:
        :return:
        """

        category = self._create_xml_tag('category', namespace='ctg')
        xml.append(category)
        self._add_elements(category, self._elements, 'ctg')

        sub_categories = self._data.get('subCategories')
        if sub_categories:
            sub_categories_element = self._create_xml_tag('subCategories', namespace='ctg')
            category.append(sub_categories_element)
            for sub_category in sub_categories:
                sub_category.category_xml(sub_categories_element)
