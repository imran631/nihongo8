import logging

from django.contrib.auth.models import User
from django.test import TestCase


logger = logging.getLogger(__name__)


class RegistTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.foo = User.objects.create(username='fooo', email='sample@example.com')

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_regist(self):
        response = self.client.get('/regist')
        self.assertEqual(response.status_code, 200)

    def test_regist_success(self):
        response = self.client.post('/regist', data={
            'username': 'new001',
            'email': 'new001@example.com',
            'password1': 'password000',
            'password2': 'password000',
            'jlpt': 'N0'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 200)

    def test_regist_same_username_email(self):
        response = self.client.post('/regist', data={
            'username': 'fooo',
            'email': 'sample@example.com',
            'password1': 'sample123!@#',
            'password2': 'sample123!@#',
            'jlpt': 'N0'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)

    def test_regist_same_only_email(self):
        response = self.client.post('/regist', data={
            'username': 'barr',
            'email': 'sample@example.com',
            'password1': 'sample123!@#',
            'password2': 'sample123!@#',
            'jlpt': 'N0'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)

    def test_regist_easy_password(self):
        response = self.client.post('/regist', data={
            'username': 'new001',
            'email': 'new001@example.com',
            'password1': '123123',
            'password2': '123123',
            'jlpt': 'N0'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)

    def test_regist_empty(self):
        response = self.client.post('/regist', data={
            'username': '',
            'email': '',
            'password1': '',
            'password2': '',
            'jlpt': ''
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)

    def test_regist_another_jlpt(self):
        response = self.client.post('/regist', data={
            'username': 'new001',
            'email': 'new001@example.com',
            'password1': 'password000',
            'password2': 'password000',
            'jlpt': 'N6'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)

    def test_regist_diff_password(self):
        response = self.client.post('/regist', data={
            'username': 'new001',
            'email': 'new001@example.com',
            'password1': 'password000',
            'password2': 'password111',
            'jlpt': 'N0'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)

    def test_regist_not_email(self):
        response = self.client.post('/regist', data={
            'username': 'new001',
            'email': '123',
            'password1': 'password000',
            'password2': 'password000',
            'jlpt': 'N0'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)

    def test_regist_not_username(self):
        response = self.client.post('/regist', data={
            'username': '1',
            'email': 'new001@example.com',
            'password1': 'password000',
            'password2': 'password000',
            'jlpt': 'N0'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)


class LoginTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.foo = User.objects.create(username='fooo', email='fooo@example.com', password='mypassword', is_active=True)
        cls.bar = User.objects.create(username='barr', email='barr@example.com', password='mypassword', is_active=False)

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)

    def test_login_fail(self):
        user = User.objects.get(username='fooo')
        print(user.email)
        print(user.username)
        print(user.password)
        print(user.is_active)
        response = self.client.post('/login', data={
            'username': 'x',
            'password': 'mypassword'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)

    def test_login_non_active(self):
        response = self.client.post('/login', data={
            'username': 'barr',
            'password': 'mypassword'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 500)
