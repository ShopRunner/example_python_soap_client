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
parser.add_argument('username', help='ShopRunner Staging Username')
parser.add_argument('password', help='ShopRunner Staging Password')

args = parser.parse_args()

wsdl_url = 'https://services.shoprunner.com/staging/services/shipment?wsdl'
client = Client(
    wsdl_url,
    wsse=UsernameToken(args.username, args.password, use_digest=True))

shipment_request_type = client.get_type('ns0:ShipmentRequestType')
shipment_type = client.get_type('ns0:Shipment')

results = client.service.Shipment(
    Partner="BLOOM",
    Shipment=[
        shipment_type(
            RetailerOrderNumber="TEST100",
            CarrierCode="UPS",
            TrackingNumber="someTrackingNumber",
            NumberOfItems=1,
            NumberOfSRItems=1,
            RetailerReferenceNumber="1234",
            RetailerNotes="NONE",
            ShippingMethod="SHOPRUNNER",
            ShipmentWeight="10")
    ])

print(results)
