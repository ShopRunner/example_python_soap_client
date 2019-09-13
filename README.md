# ShopRunner Example SOAP Client

This is an example of how to send an order to ShopRunner SOAP API in Python

# Setup
This client requires [Pipenv](https://pipenv.readthedocs.io/en/latest/) be installed

Install Dependencies:
```
pipenv install
```

# Send an order to the staging environment

```
pipenv run ./send_test_order_to_staging.py <username> <password>
```

# SR Developers: Send an order to the production environment:

Replace the wsdl url with the production wsdl url, and the order with Canary order data:
```python
wsdl_url = 'https://services.shoprunner.com/services/order?wsdl'
```
```python
results = client.service.Order(
    Partner="SRCANARYTEST",
    Order=[
        order_type(
            OrderNumber="CANARY-SOAP-2019-09-12T21:4:00-123",
            OrderDate="2019-09-12T16:58:45",
            SRAuthenticationToken="037t4ufg820r3ge87rgf9r3x",
            CurrencyCode="USD",
            TotalNumberOfItems=1,
            TotalNumberOfShopRunnerItems=1,
            OrderTax=0.0,
            OrderTotal=205.68)
    ])
```

From the jupiter database, retrieve the partner username and password for sending canaries:
```
select * from jupiter.JUPITER_PARTNER_ACCOUNT_INFO where partner_code = 'SRCANARYTEST' ;
```
Then run as above
