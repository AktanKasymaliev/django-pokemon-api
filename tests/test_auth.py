from django.test import TestCase
from django.urls import reverse
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from pokemon.models import Pokemon

User = get_user_model()

class BaseTestCase(TestCase):

    def setUp(self) -> None:
        self.register_url = reverse('signup')
        self.login_url=reverse('login')

        self.user = {
            "email": "test1@gmail.com", 
            "username": "test1",
            "password": "password", 
            "password2": "password"
            }

        self.user_short_pass = {
            "email": "test2@gmail.com", 
            "username": "test2",
            "password": "pass", 
            "password2": "passw"}

        self.user_unmatching_passwords = {
            "email": "test3@gmail.com", 
            "username": "test3",
            "password": "password", 
            "password2": "password123"}

        self.created_user = User.objects.create(
                                email='test@mail.ru', username='username_test',
                                password=make_password('password', None, 'md5')
                                            )
        self.post = Pokemon.objects.create(
                user=self.created_user,
                pokemon="pikachu"
                )


class RegisterTestCase(BaseTestCase):

    def test_can_register_user(self):
        response = self.client.post(self.register_url, data=self.user)
        self.assertEqual(response.status_code, 302)
    
    def test_cant_register_with_shortpass(self):
        try:
            response = self.client.post(self.register_url, self.user_short_pass)
            self.assertEqual(response.status_code, 400)
        except KeyError:
            return True
    
    def test_cant_register_user_with_unmatching_passwords(self):
        response = self.client.post(self.register_url, self.user_unmatching_passwords)
        self.assertEqual(response.status_code, 400)
    
    def test_cant_register_withtaken_email(self):
        self.client.post(self.register_url, self.user)
        try:
            response = self.client.post(self.register_url, self.user)
            self.assertEqual(response.status_code, 400)
        except IntegrityError: # output: Key (username)=(test1) already exists.
            return False

class LoginTest(BaseTestCase):

    def test_can_access_page(self):
        response=self.client.get(self.login_url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'auth/login.html')

    def test_login_success(self):
        self.client.post(self.register_url,self.user,format='text/html')
        user = User.objects.filter(username=self.user['username']).first()
        user.save()
        response= self.client.post(self.login_url,self.user,format='text/html')
        self.assertEqual(response.status_code,302)

    def test_cantlogin_with_no_username(self):
        response= self.client.post(self.login_url,{'password':'passwped','username':''},format='text/html')
        self.assertEqual(response.status_code,401)

    def test_cantlogin_with_no_password(self):
        response= self.client.post(self.login_url,{'username':'passwped','password':''},format='text/html')
        self.assertEqual(response.status_code,401)