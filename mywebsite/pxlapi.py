from django.http import HttpResponse
from django.shortcuts import render
 
def clientip(request):
	context = {}
	context['clientip'] = request
	return HttpResponse(request,'clientip.html',context)