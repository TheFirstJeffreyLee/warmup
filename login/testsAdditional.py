import os
import sys

sys.path.append('/home/jeffrey/cs169/djcode/mysite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.utils import unittest
from django.utils import simplejson as json
#from login.models import UsersModel
from django.test.client import Client


class testsAdditional(unittest.TestCase):

    def setUp(self):
        self.client = Client()
        self.client.post('/TESTAPI/resetFixture')

    def testAdd(self):
        req = '{"user": "seymour", "password": "butts"}'
        check = '{"count": 1, "errCode": 1}'
        response = self.client.post('/users/add', req, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, check)

    def testBadCredentials(self):
    		#bad user name
        req = '{"user": "error", "password": "butts"}'
        check = '{"errCode": -1}'
        response = self.client.post('/users/login', req, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, check)
        #bad password
        req1 = '{"user": "seymour", "password": "error"}'
        check1 = '{"errCode": -1}'
        response = self.client.post('/users/login', req1, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, check1)
    
    def testLogin(self):
        req = '{"user": "seymour", "password": "butts"}'
        check = '{"count": 2, "errCode": 1}'
        self.client.post('/users/add', req, content_type="application/json")
        response = self.client.post('/users/login', req, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, check)

    def testUserExists(self):
        req = '{"user": "seymour", "password": "butts"}'
        check = '{"errCode": -2}'
        self.client.post('/users/add', req, content_type="application/json")
        response = self.client.post('/users/add', req, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, check)


    def testBadUsername(self):
    		#case of empty name
        req = '{"user": "", "password": "anything"}'
        check = '{"errCode": -3}'
        response = self.client.post('/users/add', req, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, check)
        #case of too long name
        req1 = '{"user": "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz", "password": "anything"}'
        check1 = '{"errCode": -3}'
        response = self.client.post('/users/add', req1, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, check1)
        
        
    def testBadPassword(self):
        req= '{"user": "anything", "password": "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz"}'
        check = '{"errCode": -4}'
        response = self.client.post('/users/add', req, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, check)
    		
