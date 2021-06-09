# Pohoda XML in Python

This project is basically a rewrite of https://github.com/riesenia/pohoda into Python3 and i will try to match their versioning if possible

[![Python package](https://github.com/Salamek/pohoda/actions/workflows/python-test.yml/badge.svg)](https://github.com/Salamek/pohoda/actions/workflows/python-test.yml)


## Install


```bash
pip install pohoda
```


## Example of order import

Examples for other agenda imports in  *tests* folder.

```python
from pohoda.Pohoda import Pohoda

pohoda = Pohoda('ICO', 'i_obj1', 'Import orders')

# create order
order = pohoda.create_order({
    'numberOrder': order_number,
    'isReserved': True,
    'date': created,
    'text': '...',
    'partnerIdentity': {
        'address': {
            'name': billing_name,
            'street': billing_street,
            'city': billing_city,
            'zip': billing_zip,
            'email': email,
            'phone': phone
        },
        'shipToAddress': {
            'name': shipping_name,
            'street': shipping_street,
            'city': shipping_city,
            'zip': shipping_zip,
            'email': email,
            'phone' phone
        }
    }
})

# add items
for item in items:
    order.add_item({
        'code': item.code,
        'text': item.text,
        'quantity': item.quantity,
        'payVAT': False,
        'rateVAT': item.rate,
        'homeCurrency': {
            'unitPrice': item.unit_price
        },
        'stockItem': {
            'stockItem': {
                'id': item.pohoda_id
            }
        }
    })

# add summary
order.add_summary({
    'roundingDocument': 'none'
})

# add order to import (identified by $order_number)
pohoda.add_item(order_number, order)

# Write data into file
pohoda.write(filename)
```

## Example of stock export

Export request is made by creating *ListRequest*


```python
from pohoda.Pohoda import Pohoda

pohoda = Pohoda('ICO', 'e_zas1', 'Export stock')


request = pohoda.create_list_request({
    'type': 'Stock'
})

# optional filter
request.add_user_filter_name('MyFilter')

pohoda.add_item('Export 001', request)

pohoda.write(filename)
```


## Deleting stock example

We need to create a empty agenda with *delete* actionType to delete stock.


```python
from pohoda.Pohoda import Pohoda

pohoda = Pohoda('ICO', 'd_zas1', 'Delete stock')


stock = pohoda.create_stock([])

stock.add_action_type('delete', {
    'code': code
})

pohoda.add_item(code, stock)

pohoda.write(filename)
```
