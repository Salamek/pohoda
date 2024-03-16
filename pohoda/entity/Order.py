# coding: utf-8
from typing import List

from pohoda.entity.common.AddActionTypeTrait import AddActionTypeTrait
from pohoda.entity.Document import Document


class Order(Document, AddActionTypeTrait):
    import_root = 'lst:order'

    def _get_document_elements(self) -> List[str]:
        return super()._get_document_elements() + ['actionType']

    def _get_document_namespace(self) -> str:
        return 'ord'

    def _get_document_name(self) -> str:
        return 'order'
