# coding: utf-8

from pohoda.entity.Agenda import Agenda
from pohoda.entity.common.AddActionTypeTrait import AddActionTypeTrait
from pohoda.entity.common.AddParameterToHeaderTrait import AddParameterToHeaderTrait
from pohoda.entity.stock.Header import Header
from pohoda.entity.stock.Price import Price


class Stock(Agenda, AddActionTypeTrait, AddParameterToHeaderTrait):
    import_root = 'lStk:stock'

    def __init__(self, data: dict, ico: str):
        if data:
            data = {'header': Header(data, ico)}
        # end if
        super().__init__(data, ico)

    def add_price(self, code: str, value: float):
        """
        Add price.
        :param code:
        :param value:
        :return:
        """

        if not self._data.get('stockPriceItem'):
            self._data['stockPriceItem'] = []

        self._data['stockPriceItem'].append(Price({'code': code, 'value': value}, self._ico))
        return self

    def add_image(self, filepath: str, description: str = None, order: int = None, default: bool = False):
        """
        Add image.
        :param filepath:
        :param description:
        :param order:
        :param default:
        :return:
        """
        self._data['header'].add_image(filepath, description, order, default)
        return self

    def add_category(self, category_id: int):
        """
        Add category.
        :param category_id:
        :return:
        """

        self._data['header'].add_category(category_id)
        return self

    def add_int_parameter(self, data: dict):
        """
        Add int parameter.
        :param data:
        :return:
        """

        self._data['header'].add_int_parameter(data)
        return self

    def get_xml(self):
        xml = self._create_xml_tag('stock', namespace='stk')
        xml.set('version', '2.0')
        self._add_elements(xml, ['actionType', 'header', 'stockPriceItem'], 'stk')
        return xml
