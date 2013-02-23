from django.shortcuts import render
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from login.models import UsersModel
from login.testsAdditional import testsAdditional
import StringIO
import unittest

@csrf_exempt
def loginx(request):
	data = simplejson.loads(request.body)
	name = data['user']
	pw = data['password']
	x = UsersModel()
	response = x.login(name, pw)
	return HttpResponse(simplejson.dumps(response), content_type="application/json")


@csrf_exempt
def addx(request):
	data = simplejson.loads(request.body)
	name = data['user']
	pw = data['password']
	x = UsersModel()
	response = x.add(name, pw)
	return HttpResponse(simplejson.dumps(response), content_type="application/json")
  
  
@csrf_exempt
def TESTAPI_resetFixturex(request):
	x = UsersModel()
	response = x.TESTAPI_resetFixture()
	return HttpResponse(simplejson.dumps(response), content_type="application/json")

@csrf_exempt	
def TESTAPI_unitTests(request):
	buffer = StringIO.StringIO()
	tests = unittest.TestLoader().loadTestsFromTestCase(testsAdditional)
	result = unittest.TextTestRunner(stream = buffer, verbosity = 2).run(tests)
	response = {"totalTests": result.testsRun, "nrFailed": len(result.failures), "output": buffer.getvalue()}
	return HttpResponse(json.dumps(response), content_type = "application/json")
