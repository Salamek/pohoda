# coding: utf-8
from pohoda.entity.Document import Document


class Bank(Document):
    import_root = 'lst:bank'

    def _get_document_name(self) -> str:
        return 'bank'

    def _get_document_namespace(self) -> str:
        return 'bnk'
