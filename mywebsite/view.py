from django.http import HttpResponse
from django.shortcuts import render_to_response
 
def hello(request):
    return HttpResponse("Hello world ! ")
def page_not_found(request):
	html = u"<html><h1>��Ҫ�Ķ�����������<h1></html>".encode()
	return HttpResponse(html)