'''gdapi client config stuff'''
import os

DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE')

def get_config(url=None,access_key=None,secret_key=None):
    return {
        'url': url or os.getenv('GDAPI_URL'),
        'access_key': access_key or os.getenv('GDAPI_ACCESS_KEY'),
        'secret_key': secret_key or os.getenv('GDAPI_SECRET_KEY')
    }

