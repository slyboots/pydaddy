#! python3
import os
import requests

# Dev api info
GD_API = os.getenv('GDAPI_URL')
GD_KEY = os.getenv('GDAPI_ACCESS_KEY')
GD_SECRET = os.getenv('GDAPI_SECRET_KEY')
# Api environment
DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE')


class Pydaddy():
    '''root pydaddy app class'''
    def _init__(self):
        pass


def raise_for_rate_limit(api_response):
 '''checks if response status_code is 429
 this means the rate limit (60 request / minute) for the API has been reached'''
 if api_response.status_code == 429:
   print('ERROR REQUEST RATE LIMIT EXCEEDED')
   print(api_response.content)


"""
There are two types of users of the API. It is important to understand the which category you fall under so you can use the API correctly.
Self-Serve: You are authenticated as and operating on your own account. You can ignore references to Subaccounts and theX-Shopper-Idheader.
Reseller: You authenticated as and operating on behalf of one of your customers. You will need to create a Subaccount to represent your end user and specify its ShopperId X-Shopper-Id in your API calls.
"""