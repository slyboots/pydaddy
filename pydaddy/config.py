'''gdapi client config stuff'''
import os

DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE')

def get_config(url=None,access_key=None,secret_key=None):
    return {
        'GDAPI_URL': url or os.getenv('GDAPI_URL'),
        'GDAPI_ACCESS_KEY': access_key or os.getenv('GDAPI_ACCESS_KEY'),
        'GDAPI_SECRET_KEY': secret_key or os.getenv('GDAPI_SECRET_KEY')
    }

