#encoding:utf-8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
 
def hello(request):
    return HttpResponse("Hello world ! ")
def page_not_found(request,exception):
	html = u"<html><h1>你要的东西并不存在<h1></html>".encode()
	data = '你要的东西并不存在'
	return render_to_response('404.html',{'mydata':data})
def page_error(request):
	html = u"<html><h1>你要的东西并不存在<h1></html>".encode()
	data = '你要的东西并不存在'
	return render(html)