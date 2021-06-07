# coding: utf-8
from typing import Optional
from lxml import etree
from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddParameterTrait import AddParameterTrait
from pohoda.entity.stock.Category import Category
from pohoda.entity.stock.IntParameter import IntParameter
from pohoda.entity.stock.Picture import Picture


class Header(Agenda, AddParameterTrait):
    _ref_elements = ['storage', 'typePrice', 'typeRP', 'supplier']
    _elements_attributes_mapper = {'purchasingPricePayVAT': ['purchasingPrice', 'payVAT'],
                                   'sellingPricePayVAT': ['sellingPrice', 'payVAT']}
    _elements = ['stockType', 'code', 'EAN', 'PLU', 'isSales', 'isSerialNumber', 'isInternet', 'isBatch',
                 'purchasingRateVAT', 'sellingRateVAT', 'name', 'nameComplement', 'unit', 'unit2', 'unit3',
                 'coefficient2', 'coefficient3', 'storage', 'typePrice', 'purchasingPrice', 'purchasingPricePayVAT',
                 'sellingPrice', 'sellingPricePayVAT', 'limitMin', 'limitMax', 'mass', 'volume', 'supplier',
                 'orderName', 'orderQuantity', 'shortName', 'typeRP', 'guaranteeType', 'guarantee', 'producer',
                 'description', 'description2', 'note']
    _images_counter = 0

    def add_image(self,
                  filepath: str,
                  description: Optional[str] = None,
                  order: Optional[int] = None,
                  default: bool = False
                  ) -> None:
        """
        Add image.
        :param filepath:
        :param description:
        :param order:
        :param default:
        :return:
        """
        if not self._data.get('pictures'):
            self._data['pictures'] = []

        if not order:
            self._images_counter += 1
            order = self._images_counter

        self._data['pictures'].append(Picture(
            {
                'filepath': filepath,
                'description': description,
                'order': order,
                'default': default
            },
            self._ico
        ))

    def add_category(self, category_id: int) -> None:
        """
        Add category.
        :param category_id:
        :return:
        """
        if not self._data.get('categories'):
            self._data['categories'] = []

        self._data['categories'].append(Category(
            {
                'idCategory': category_id
            },
            self._ico
        ))

    def add_int_parameter(self, data: dict) -> None:
        """
        Add int parameter.
        :param data:
        :return:
        """

        if not self._data.get('intParameters'):
            self._data['intParameters'] = []

        self._data['intParameters'].append(IntParameter(data, self._ico))

    def get_xml(self) -> etree.Element:
        xml = self._create_xml_tag('stockHeader', namespace='stk')
        self._add_elements(xml, self._elements + ['categories', 'pictures', 'parameters', 'intParameters'], 'stk')
        return xml
