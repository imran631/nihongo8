import logging

from django.test import TestCase


logger = logging.getLogger(__name__)


class AuthTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_regist(self):
        logger.debug('called regist')
        response = self.client.get('/regist')
        self.assertEqual(response.status_code, 200)

    def test_regist_api(self):
        logger.debug('called regist_api')
        response = self.client.post('/regist', data={
            'username': 'sample',
            'email': 'sample@naver.com',
            'password1': 'sample123!@#',
            'password2': 'sample123!@#',
            'jlpt': 'N0'
        })
        logger.debug(response.json())
        self.assertEqual(response.json()['result'], 200)