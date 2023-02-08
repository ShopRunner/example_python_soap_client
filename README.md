# ShopRunner Example SOAP Client

This is an example of how to send an order to ShopRunner SOAP API in Python

# Setup
This client requires [Pipenv](https://pipenv.readthedocs.io/en/latest/) be installed

you may have to run 
```shell
pipenv shell 
```
Before Installing Dependencies:
```shell
pipenv install
```

# Send an order to the staging environment

```
pipenv run ./send_test_order_to_staging.py <username> <password>
```

# Send an order adjustment to the staging environment

```
pipenv run ./send_test_order_adjustment_to_staging.py <username> <password>
```