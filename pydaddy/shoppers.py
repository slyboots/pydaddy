import json
import requests

from .app import build_headers, build_url

SHOPPER_ACTIONS = {
    'CREATE_SUBACCOUNT': {
        'method': 'POST',
        'url': '/v1/shoppers/subaccount'
    },
    'GET_SUBACCOUNT': {
        'method': 'GET',
        'url': '/v1/shoppers/{shopper_id}'
    }
}
class Shoppers(object):
    '''interface for GoDaddy shoppers api'''
    @classmethod
    def create(cls, email, name_first, name_last, password, market_id='en-us',external_id=None):
        ''' creates a subaccount for accessing customer account details
        example shopper:
        {
            "email": "dakota@mailinator.com",
            "externalId": 10110,
            "marketId": "en-us",
            "nameFirst": "Dakota",
            "nameLast": "Mail",
            "password": "FGCAdsvcsdcfa$htghbfg"
        }
        example response:
        {
            "shopperId": "ett45tg",
            "customerId": "ewe43b2-5fa7-erte-a4e9-aerf45t45442"
        }
        '''
        method = SHOPPER_ACTIONS['CREATE_SUBACCOUNT'].get('method')
        url = build_url(SHOPPER_ACTIONS['CREATE_SUBACCOUNT'].get('url'))
        headers = build_headers(json=True)
        subaccount_info = {
            'email': email,
            'marketId': market_id,
            'nameFirst': name_first,
            'nameLast': name_last,
            'password': password
        }
        if external_id:
            subaccount_info.update({'externalId': external_id})

        api_response = requests.request(method=method,url=url,headers=headers,data=json.dumps(subaccount_info))
        return api_response
