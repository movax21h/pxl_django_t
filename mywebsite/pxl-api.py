from django.http import HttpResponse
 
def clientip(request):
	context = []
	context['clientip'] = dir(request)
    return HttpResponse(request,'clientip.html',context)