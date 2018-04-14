import requests

# api endpoints
ACTIONS = {
    'DOMAIN_AVAILABLE': {
        'url': '/domains/available?domain={domain}',
        'method': 'GET'
    }
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