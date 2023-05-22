import requests
import json

class ShoppyAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://shoppy.gg/api/v1/'

    def get_products(self):
        url = self.base_url + 'products'
        headers = {'Authorization': self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_product(self, product_id):
        url = self.base_url + f'products/{product_id}'
        headers = {'Authorization': self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def create_product(self, title, price, description, stock):
        url = self.base_url + 'products'
        headers = {'Authorization': self.api_key, 'Content-Type': 'application/json'}
        data = {'title': title, 'price': price, 'description': description, 'stock': stock}
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    
    def delete_product(self, product_id):
        url = self.base_url + f'products/{product_id}'
        headers = {'Authorization': self.api_key}
        response = requests.delete(url, headers=headers)
        return response.json()
    
    def update_product_stock(self, product_id, new_stock):
        url = self.base_url + f'products/{product_id}'
        headers = {'Authorization': self.api_key, 'Content-Type': 'application/json'}
        data = {'stock': new_stock}
        response = requests.patch(url, headers=headers, json=data)
        return response.json()

    def search_products(self, query):
        url = self.base_url + 'products'
        headers = {'Authorization': self.api_key}
        params = {'query': query}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def create_order(self, product_id, email):
        url = self.base_url + 'orders/create'
        headers = {'Authorization': self.api_key, 'Content-Type': 'application/json'}
        data = {'product_id': product_id, 'email': email}
        response = requests.post(url, headers=headers, json=data)
        return response.json()
    
    def get_order(self, order_id):
        url = self.base_url + f'orders/{order_id}'
        headers = {'Authorization': self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def update_order_status(self, order_id, status):
        url = self.base_url + f'orders/{order_id}'
        headers = {'Authorization': self.api_key, 'Content-Type': 'application/json'}
        data = {'status': status}
        response = requests.put(url, headers=headers, json=data)
        return response.json()

    def get_user_profile(self):
        url = self.base_url + 'user'
        headers = {'Authorization': self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def get_user_orders(self, user_id):
        url = self.base_url + f'users/{user_id}/orders'
        headers = {'Authorization': self.api_key}
        response = requests.get(url, headers=headers)
        return response.json()

    def parse_data(self, data):
        json_data = json.dumps(data)
        parsed_data = json.loads(json_data)

        title = parsed_data['title']
        description = parsed_data['description']
        image_url = parsed_data['image']['url']
        price = parsed_data['price']
        stock = parsed_data['stock']
        currency = parsed_data['currency']
        seller = parsed_data['seller']

        print(f"Title: {title}")
        print(f"Description: {description}")
        print(f"Image URL: {image_url}")
        print(f"Price: {price} {currency}")
        print(f"Stock: {stock}")
        print(f"Seller: {seller}")