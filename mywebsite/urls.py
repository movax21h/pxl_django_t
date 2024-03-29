"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import view
from . import pxlapi
from . import testdb
from django.conf.urls import handler404,handler500

urlpatterns = [
	url(r'^$',view.hello),
	url(r'^ip$',pxlapi.clientip),
	url(r'^addname',testdb.testdb),
	url(r'^read',testdb.testread),]
handler404 = 'mywebsite.view.page_not_found'
handler500 = 'mywebsite.view.page_error'
	#path('admin/', admin.site.urls),
