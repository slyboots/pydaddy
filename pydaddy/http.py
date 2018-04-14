import os
import json
import requests
from requests.auth import AuthBase

class GodaddyAuth(AuthBase):
    '''add custom authorization header to request'''
    def __init__(self, key=None, secret=None):
        self.key = key or os.getenv('GDAPI_ACCESS_KEY')
        self.secret = secret or os.getenv('GDAPI_SECRET_KEY')


    def __call__(self, r):
        r.headers['Authorization'] = f"sso-key {self.key}:{self.secret}"
        return r


def build_headers(json=None):
    '''builds request headers'''
    api_key = os.getenv('GDAPI_ACCESS_KEY')
    api_secret = os.getenv('GDAPI_SECRET_KEY')
    headers = {
        'Authorization': f'sso-key {api_key}:{api_secret}',
        'Accept': 'application/json'
    }
    if json:
        headers.update({'Content-Type': 'application/json'})
    return headers

def build_url(endpoint, **kwargs):
    '''build url for api requests'''
    return os.getenv('GDAPI_URL') + endpoint.format(**kwargs)

def construct_request(action, data=None, **kwargs):
    '''build and send request to gdapi'''
    url = build_url(action['url'], **kwargs)
    body = json.dumps(data or {})
    res = requests.request(method=action['method'], url=url, auth=GodaddyAuth(), data=body)
    return res