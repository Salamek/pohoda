

from pohoda.entity.document.Summary import Summary as DocumentSummary


class Summary(DocumentSummary):
    _elements = ['roundingDocument', 'roundingVAT', 'homeCurrency', 'foreignCurrency']

