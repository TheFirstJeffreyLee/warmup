from django.db import models
from django.http import HttpResponse
from django.utils import simplejson as json
from django.forms.models import model_to_dict
import StringIO
import unittest

SUCCESS               =   1 
ERR_BAD_CREDENTIALS   =  -1  
ERR_USER_EXISTS       =  -2  
ERR_BAD_USERNAME      =  -3  
ERR_BAD_PASSWORD      =  -4

class UsersModel(models.Model):
	user = models.CharField(primary_key=True, max_length=128)
	password = models.CharField(max_length=128)
	count = models.IntegerField()		

	def login(self, user1, password1):
		try:
			obj = UsersModel.objects.get(user=user1) #success getting obj means correct user
			user_info = model_to_dict(obj)
		except:
			return {'errCode': ERR_BAD_CREDENTIALS}
		if user_info['password'] == password1:
			obj.count = obj.count + 1
			obj.save()
			return {'errCode': SUCCESS, 'count': obj.count}
		else:
			return {'errCode': ERR_BAD_CREDENTIALS}
	
	
	def add(self, user1, password1):
		exist = True 
		try:
			obj = UsersModel.objects.get(user=user1) #success means already exists
			user_info = model_to_dict(obj)
		except:
			exist = False
		if exist:
			return {'errCode': ERR_USER_EXISTS}
		elif len(password1) > 128:
			return {'errCode': ERR_BAD_PASSWORD}
		elif user1 == '' or len(user1) > 128:
			return {'errCode': ERR_BAD_USERNAME}
		else:
			new = UsersModel(user = user1, password = password1, count = 1)
			new.save()
			return {'errCode': SUCCESS, 'count': 1}

	def TESTAPI_resetFixture(request):
		UsersModel.objects.all().delete()
		return {'errCode': SUCCESS}





