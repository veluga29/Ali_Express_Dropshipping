import requests
import json
from ..settting import API_KEY

# zapiex.py classify HW

class ZapiexAPI:
    headers = {'x-api-key': API_KEY}
    def __init__():
        pass

    def get_product(product_id: str):
        URL = 'https://api.zapiex.com/v3/product/details'
        data = {'productId': product_id, 'getHtmlDescription': 'true'}
        response = requests.post(URL, headers=headers, data=data)
        return response.json()
    
    #def get_product_shipping_info
    #def get_product_reviews
    
    
    def search_products(text: str):
        pass
    
    #def search_products_by_store


# zapiex_apis = ZapiexAPI()

def get_product(product_id: str):
    URL = 'https://api.zapiex.com/v3/product/details'
    headers = {'x-api-key': API_KEY}
    data = {'productId': product_id, 'getHtmlDescription': 'true'}
    response = requests.post(URL, headers=headers, data=data)
    return response.json()


def search_products(text: str):
    URL = 'https://api.zapiex.com/v3/search'
    headers = {'x-api-key': API_KEY}
    data = {'text': text}
    response = requests.post(URL, headers=headers, data=json.dumps(data))  # 왜 dump해야 오류 없을까요
    return response.json()
