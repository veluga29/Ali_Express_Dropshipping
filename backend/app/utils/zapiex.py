import requests
import json
from app.settings import API_KEY


class ZapiexAPI:
    headers = {"x-api-key": API_KEY}

    def search_products(self, text: str, page: int):
        URL = "https://api.zapiex.com/v3/search"
        data = {"text": text, "shipTo": "KR", "page": page}
        response = requests.post(URL, headers=ZapiexAPI.headers, data=json.dumps(data))
        return response.json()

    def get_product(self, product_id: str):
        URL = "https://api.zapiex.com/v3/product/details"
        data = {
            "productId": product_id,
            "shipTo": "KR",
            "getSellerDetails": "true",
            "getShipping": "true",
            "getHtmlDescription": "true",
        }
        response = requests.post(URL, headers=ZapiexAPI.headers, data=data)
        return response.json()


zapiex_apis = ZapiexAPI()
