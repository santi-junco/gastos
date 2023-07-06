# import requests, json

from rest_framework.test import APITestCase, APIClient
from django.conf import settings

class Login(APITestCase):
    url = f'{settings.URL}/login/'
    client = APIClient()

    def __init__(self, email, password, to_assert=200):
        data = {
            'email': email,
            'password': password
        }
        response = self.client.post(self.url, data, format='json')

        if response.status_code == to_assert:
            if response.status_code == 200:
                self.token = response.json()['access']
        else:
            raise ValueError(response.status_code, response.content.decode("utf-8"))
        