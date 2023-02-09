#!/usr/bin/env python3
import argparse
from zeep import Client
from zeep.wsse.username import UsernameToken
import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

parser = argparse.ArgumentParser(description='ShopRunner SOAP Example')
parser.add_argument('env', help='Environment: wip or stg', choices=['wip', 'stg'])
parser.add_argument('orderid', help='Retailer Order Number')
parser.add_argument('username', help='ShopRunner Staging Username')
parser.add_argument('password', help='ShopRunner Staging Password')

args = parser.parse_args()

url = 'https://orderservices.stg.shoprunner.io' if args.env == 'stg' else 'https://orderservices.wip.shoprunner.io'
wsdl_url = url + "/services/order?wsdl"
client = Client(
    wsdl_url,
    wsse=UsernameToken(args.username, args.password, use_digest=True))

order_request_type = client.get_type('ns0:OrderRequestType')
order_type = client.get_type('ns0:Order')
adjustment_type = client.get_type('ns0:Adjustment')

results = client.service.Order(
    Partner="SRCANARYTEST",
    Order=[
        order_type(
            OrderNumber=args.orderid,
            OrderDate="2023-01-10T16:58:45",
            SRAuthenticationToken="",
            CurrencyCode="USD",
            TotalNumberOfItems=2,
            TotalNumberOfShopRunnerItems=2,
            OrderTax=0.0,
            OrderTotal=205.68,
            Adjustment=adjustment_type(
                           AdjustmentId=12345678,
                           AdjustmentAmount=-100.00,
                           BillingAdjustmentAmount=-100.00,
                           AdjustmentType="CANCEL"
                       )
        ),

    ])


print(results)
print('----')

print(wsdl_url)
print(results['Partner'], results['Order'][0]['OrderNumber'])
print('OrderDate', results['Order'][0]['OrderDate'])
print('OrderDate', results['Order'][0]['OrderTotal'])
print('AdjustmentType', results['Order'][0]['Adjustment'][0]['AdjustmentType'])
