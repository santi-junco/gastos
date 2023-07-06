import unittest, datetime

from tests.Classes.Ingreso import Ingreso
from tests.Classes.User import User
from tests.Classes.Login import Login

class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        global user
        global login_user
        
        user = User(
            email="ingreso@mail.com",
            password="santi123",
            first_name="santiago leonel",
            last_name="junco"
        )
        
        login_user = Login(email="ingreso@mail.com", password="santi123")

    def test_1(self):
        """Testea el indpoint api/v1/movimientos/ingreso/create/ para el metodo post
        status code esperado 200, 400, 401 o 403
        """
        Ingreso(
            token=login_user.token,
            usuario=user.id,
            descripcion='ingreso 1',
            fecha=datetime.datetime.today().date(),
            monto=1243.2
        )
    
    def test_2(self):
        """Testea el indpoint api/v1/movimientos/ingreso/list/ para el metodo get
        status code esperado 200, 400, 401 o 403
        """
        ingreso = Ingreso(
            token=login_user.token,
            usuario=user.id,
            descripcion='ingreso 2',
            fecha=datetime.datetime.today().date(),
            monto=1243.2
        )
        
        ingreso.get_ingresos(login_user.token)
    
    def test_3(self):
        """Testea el indpoint api/v1/movimientos/ingreso/update/<pk>/ para el metodo patch
        status code esperado 200, 400, 401 o 403
        """
        ingreso = Ingreso(
            token=login_user.token,
            usuario=user.id,
            descripcion='ingreso 3',
            fecha=datetime.datetime.today().date(),
            monto=1243.2
        )
        
        ingreso.edit_ingreso(token=login_user.token, descripcion='ingreso 3 editado')

    def test_4(self):
        """Testea el indpoint api/v1/movimientos/ingreso/delete/<pk>/ para el metodo delete
        status code esperado 200, 400, 401 o 403
        """
        ingreso = Ingreso(
            token=login_user.token,
            usuario=user.id,
            descripcion='ingreso 4',
            fecha=datetime.datetime.today().date(),
            monto=1243.2
        )
        
        ingreso.delete_ingreso(token=login_user.token)
