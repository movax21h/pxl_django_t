#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
from datamodel.models import test
 
def testdb(request):
	test1 = test(name='xiaolong')
	test1.save()
	return HttpResponse('<p>add data success</p>')
def testread(request):
	response=''
	list = test.object.all()
	for var in list:
		response += var
	return HttpResponse('<p>'+response+'</p>')