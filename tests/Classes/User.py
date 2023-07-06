import os, django, json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.test')
django.setup()

from django.conf import settings
from rest_framework.test import APITestCase, APIClient

class User(APITestCase):
    url = f"{settings.URL}/users"
    client = APIClient()
    
    def __init__(self, email, password, first_name, last_name, to_assert=201):
        url = f"{self.url}/register/"
        data = {
            'email': email,
            'password': password,
            'first_name': first_name,
            'last_name': last_name,
        }
        
        response = self.client.post(url, data, format='json')

        if response.status_code == to_assert:
            if response.status_code == 201:
                self.id = json.loads(response.content)['id']
                self.email: email
                self.password: password
                self.first_name: first_name
                self.last_name: last_name
        else:
            raise ValueError(response.status_code, response.content.decode("utf-8"))
    
    def get_user(self, token, to_assert=200):
        url = f"{self.url}/view/{self.id}/"
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {token}")
        
        if response.status_code != to_assert:
            raise ValueError(response.status_code, response.content.decode("utf-8"))
        
        return json.loads(response.content)
    
    def update_user(self, token, email=None, password=None, first_name=None, last_name=None, to_assert=200):
        body_params = locals()
        body = {k:v for k,v in body_params.items() if k not in ['self', 'token', 'to_assert'] and v is not None}
        url = f'{self.url}/update/{self.id}/'
        
        response = self.client.patch(url, body, HTTP_AUTHORIZATION=f"Bearer {token}")
        
        if response.status_code == to_assert:
            if response.status_code == 200:
                body = json.loads(response.content)
                self.email = body['email']
                self.password = body['password']
                self.first_name = body['first_name']
                self.last_name = body['last_name']
        else:
            raise ValueError(response.status_code, response.content.decode("utf-8"))
    
    def delete_user(self, token, to_assert=204):
        url = f"{self.url}/delete/{self.id}/"
        response = self.client.delete(url, HTTP_AUTHORIZATION=f"Bearer {token}")

        if response.status_code != to_assert:
            raise ValueError(response.status_code, response.content.decode("utf-8"))
