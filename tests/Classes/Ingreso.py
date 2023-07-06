import os, django, json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.test')
django.setup()

from rest_framework.test import APITestCase, APIClient

from django.conf import settings

class Ingreso(APITestCase):
    url = f'{settings.URL}/movimientos/ingresos/'
    client = APIClient()
    
    def __init__(self, token, usuario, descripcion, fecha, monto, to_assert=201):
        url = f"{self.url}create/"
        data = {
            "usuario": usuario,
            "descripcion": descripcion,
            "fecha": fecha,
            "monto": monto
        }
        response = self.client.post(url, data, HTTP_AUTHORIZATION=f"Bearer {token}")
        
        if response.status_code == to_assert:
            if response.status_code == 201:
                self.id = json.loads(response.content)['id']
                self.usuario = usuario,
                self.descripcion = descripcion,
                self.fecha = fecha,
                self.monto = monto
        else:
            raise ValueError(response.status_code, response.content.decode('utf-8'))
    
    def get_ingresos(self, token, to_assert=200):
        url = f'{self.url}list/'
        response = self.client.get(url, HTTP_AUTHORIZATION=f"Bearer {token}")
        
        if response.status_code == to_assert:
            if response.status_code == 200:
                return json.loads(response.content)
        else:
            raise ValueError(response.status_code, response.content.decode("utf-8"))
    
    def edit_ingreso(self, token, descripcion=None, fecha=None, monto=None, to_assert=200):
        body_params = locals()
        data = {k:v for k,v in body_params.items() if k not in ['self', 'token', 'to_assert'] and v}
        url = f'{self.url}update/{self.id}/'
        response = self.client.patch(url, data, HTTP_AUTHORIZATION=f"Bearer {token}")
        
        if response.status_code == to_assert:
            if response.status_code == 200:
                self.descripcion = descripcion if descripcion else self.descripcion
                self.fecha = fecha if fecha else self.fecha
                self.monto = monto if monto else self.monto
        else:
            raise ValueError(response.status_code, response.content.decode("utf-8"))
    
    def delete_ingreso(self, token, to_assert=204):
        url = f'{self.url}delete/{self.id}/'
        response = self.client.delete(url, HTTP_AUTHORIZATION=f"Bearer {token}")

        if response.status_code != to_assert:
            raise ValueError(response.status_code, response.content.decode("utf-8"))
    