import requests
from .app import build_headers, build_url

# api endpoints
GD_ENDPOINTS = {
 'DOMAIN_AVAILABLE': '/domains/available?domain={domain}'
}

def get_domain_available(domain):
    ''' check domain availability on godaddy
    example response:
    {
        "available":falslse,
        "domain":"dakotalorance.com",
        "definitive":true,
        "price":10690000,
        "currency":"USD",
        "period":1
    }'''
    header = build_headers()
    endpoint = build_url('DOMAIN_AVAILABLE', domain=domain)
    res = requests.get(endpoint,headers=header)
    res.raise_for_status()
    print(res.headers)
    print(res.content)