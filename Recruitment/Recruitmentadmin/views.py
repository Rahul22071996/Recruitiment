from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.conf import settings
from . import models
from Applicant.models import *
from . models import *
from .models import Bussines_content
from .forms import openings_form
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.models import User ,auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .decorators import unauthenticated_user ,allowed_users
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .middlewares import login_register_middleware
from django.shortcuts import get_list_or_404, get_object_or_404
media_url=settings.MEDIA_URL
curl=settings.CURRENT_URL


# # admin home
# @login_required(login_url='./login')
# @allowed_users(allowed_roles='admin')
@login_required(login_url='/Recuritment/admin/login')

@allowed_users(allowed_roles='admin')

def home(request):
	

	return render(request,'dashbord.html')



# # this is for freelancer
@login_required(login_url='/Recuritment/admin/login')

@allowed_users(allowed_roles='admin')


def Opening(request):
	if request.method == "POST":
		form = openings_form(request.POST or None, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('/')
		return render(request,'Opening-list1.html',{'form':form})
	else:
		form = openings_form(request.POST or None, request.FILES or None)
		return render(request,'Opening-list1.html',{'form':form})


####################views old opeanings###################




# obj = get_object_or_404(GeeksModel, id = id)
 
#     # pass the object as instance in form
#     form = GeeksForm(request.POST or None, instance = obj)
 
#     # save the data from the form and
#     # redirect to detail_view
#     if form.is_valid():
#         form.save()
#         return HttpResponseRedirect("/"+id)
 
#     # add form dictionary to context
#     context["form"] = form
@login_required(login_url='/Recuritment/admin/login')
@allowed_users(allowed_roles='admin')
def View_Openings(request,id):
	obj = get_object_or_404(AddVacancyPosition, id = id)
	form = openings_form(request.POST or None, request.FILES or None,instance=obj)
	if form.is_valid():
		form.save()
		return redirect('/')

	return render(request,'View_Openings.html',{'form':form,'id':id})
@login_required(login_url='/Recuritment/admin/login')
@allowed_users(allowed_roles='admin')
def All_Openings(request):
	All_Data = AddVacancyPosition.objects.all()
	return render(request,'All_Openings.html',{'All_Data':All_Data})

# this is for delete data of table
@login_required(login_url='/Recuritment/admin/login')
@allowed_users(allowed_roles='admin')
def HandleDelete(request,id):
	try:
		data = AddVacancyPosition.objects.get(id=id).delete()

		return redirect('/Recuritment/admin/All_Openings/')
	except Exception as e:
		return HttpResponse(e)


##########Admin LOGIN #######################
# @login_required(login_url='/Recuritment/admin/login')
# @allowed_users(allowed_roles='admin')
def handlelogin(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=auth.authenticate(request,username=username,password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('/Recuritment/admin')
		else:
			return redirect('/Recuritment/admin/login')
		# else:
		# 	print('invalide password')
		# 	return render(request,'login.html')
		
	else:
		return render(request,'login.html',{'curl':curl})

##############Admin Logout###############

@login_required(login_url='/Recuritment/admin/login')
def logout(request):
	auth.logout(request)
	return redirect('/Recuritment/admin/')



