import unittest

from tests.Classes.User import User
from tests.Classes.Login import Login

class Tests(unittest.TestCase):
    
    def test_1(self):
        """Testea el endpoint ap1/v1/users/register/ para el metodo post
        status code esperado 200
        """
        global user
        global user2
        
        user = User(
            email="email@mail.com",
            password="santi123",
            first_name="santiago leonel",
            last_name="junco"
        )

        user2 = User(
            email="email2@mail.com",
            password="santi123",
            first_name="santiago",
            last_name="junco"
        )

    def test_2(self):
        """Testea el endpoint ap1/v1/users/register/ para el metodo post
        status code esperado 400
        """
        User(
            email="email@mail.com",
            password="santi123",
            first_name="",
            last_name="junco",
            to_assert=400
        )

    def test_3(self):
        """Testea el endpoint ap1/v1/login/ para el metodo post
        status code esperado 200, 400
        """
        global login_user
        global login_user2
        
        login_user = Login(email="email@mail.com", password="santi123")
        login_user2 = Login(email="email2@mail.com", password="santi123")

    def test_4(self):
        """Testea el endpoint ap1/v1/users/view/<pk>/ para el metodo get
        status code esperado 200, 404
        """
        user.get_user(login_user.token)
        user.get_user(login_user2.token, to_assert=404)

    def test_5(self):
        """Testea el endpoint ap1/v1/users/update/<pk>/ para el metodo patch
        status code esperado 200, 400, 404
        """
        user.update_user(login_user.token)
        user.update_user(login_user.token, first_name="santi")
        user.update_user(login_user.token, email="", to_assert=400)
        user.update_user(login_user2.token, to_assert=404)

    def test_6(self):
        """Testea el endpoint api/v1/users/delete/<pk>/ para el metodo delete
        status code esperado 204, 404
        """
        user.delete_user(login_user2.token, to_assert=404)
        user.delete_user(login_user.token)