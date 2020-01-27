#!/usr/bin/env python3
import argparse
from zeep import Client
from zeep.wsse.username import UsernameToken
from freezegun import freeze_time
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
parser.add_argument('username', help='ShopRunner Staging Username')
parser.add_argument('password', help='ShopRunner Staging Password')

args = parser.parse_args()

wsdl_url = 'http://localhost:8080/services/order?wsdl'

client = Client(
    wsdl_url,
    wsse=UsernameToken(args.username, args.password, use_digest=True))

order_request_type = client.get_type('ns0:OrderRequestType')
order_type = client.get_type('ns0:Order')
order_token = client.get_type('ns0:OrderToken')

print(order_token)

@freeze_time("2012-01-14")
def sendOrder():
    results = client.service.Order(
        Partner="SRCANARYTEST",
        Order=[
            order_type(
                OrderNumber="TEST100",
                OrderDate="2014-01-10T16:58:45",
                SRAuthenticationToken="037t4ufg820r3ge87rgf9r3x",
                CurrencyCode="USD",
                TotalNumberOfItems=1,
                TotalNumberOfShopRunnerItems=1,
                OrderTax=0.0,
                OrderToken = [order_token(TokenType="sameday", TokenValue="abcdef")],
                OrderTotal=205.68)
        ])
    print(results)

sendOrder()
