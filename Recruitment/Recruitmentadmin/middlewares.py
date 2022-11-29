from django.shortcuts import HttpResponseRedirect
from django.urls import resolve
def login_register_middleware(get_response):
	def middleware(request):
		url_name=resolve(request.path_info).url_name
		if(url_name =='Dailyadmin/login') and request.user.is_authenticated:
			response=HttpResponseRedirect('/Dailyadmin')
		else:
			response =get_response(request)
		return response
	return middleware