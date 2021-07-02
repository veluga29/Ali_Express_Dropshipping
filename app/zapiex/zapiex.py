import requests
import json
from ..settings import API_KEY

# zapiex.py classify HW
class ZapiexAPI:
    headers = {'x-api-key': API_KEY}
    
    def get_product(self, product_id: str):
        URL = 'https://api.zapiex.com/v3/product/details'
        data = {'productId': product_id, 'shipTo': 'KR', 'getSellerDetails': 'true'
                , 'getShipping': 'true', 'getHtmlDescription': 'true'}
        response = requests.post(URL, headers=ZapiexAPI.headers, data=data)
        return response.json()
    
    def get_product_shipping_info(self, product_id: str):
        URL = 'https://api.zapiex.com/v3/product/shipping'
        data = {'productId': product_id, 'shipTo': 'KR'}
        response = requests.post(URL, headers=ZapiexAPI.headers, data=data)
        return response.json()
    
    def get_product_reviews(self, product_id: str):
        URL = 'https://api.zapiex.com/v3/product/reviews'
        data = {'productId': product_id}
        response = requests.post(URL, headers=ZapiexAPI.headers, data=data)
        return response.json()
    
    def search_products(self, text: str):
        URL = 'https://api.zapiex.com/v3/search'
        data = {'text': text, 'shipTo': 'KR'}
        response = requests.post(URL, headers=ZapiexAPI.headers, data=json.dumps(data))  # 왜 dump해야 오류 없을까요
        return response.json()
    
    def search_products_by_store(self, store_id: str, text: str):
        URL = 'https://api.zapiex.com/v3/search-by-store'
        data = {'storeId': store_id, 'text': text}
        response = requests.post(URL, headers=ZapiexAPI.headers, data=json.dumps(data))
        return response.json()


zapiex_apis = ZapiexAPI()
