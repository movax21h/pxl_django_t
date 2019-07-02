from django.http import HttpResponse
from django.shortcuts import render
 
def clientip(request):
	context = {}
	context['clientip'] = dir(request.GET())
	return render(request,'clientip.html',context)