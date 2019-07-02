from django.http import HttpResponse
from django.shortcuts import render
 
def clientip(request):
	context = {}
	try:	
		if 'HTTP_X_FORWARDED_FOR' in request.META:
			context['clientip'] = request.META.get('HTTP_X_FORWARDED_FOR')
		else:
			context['clientip'] = request.META.get('REMOTE_ADDR')
	except:
		context['clientip'] = 'NONE'
	
	return render(request,'clientip.html',context)
