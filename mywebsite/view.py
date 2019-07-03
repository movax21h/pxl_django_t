from django.http import HttpResponse
from django.shortcuts import render_to_response
 
def hello(request):
    return HttpResponse("Hello world ! ")
def page_not_found(request,**kwargs):
	html = "<html><h1>你要的东西并不存在<h1></html>"
	return HttpResponse(html)