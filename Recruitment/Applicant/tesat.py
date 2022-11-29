from django.shortcuts import render ,redirect
from django.http import HttpResponse
from Recruitmentadmin.models import add ,contact_us,admin_block,Banner_data,Social_Links,footer_data,Add_category,Bussines_content
from Recruitmentadmin.models import Postjobs
from django.conf import settings
from .models import userprofile,assignproject
from django.core.files.storage import FileSystemStorage
from .models import user_enquiry 
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
from .import models
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User ,auth
from .forms import user_enquiry_form ,CreateUserform ,userprofileform ,Userupdateform ,Userprofileupdateform
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.contrib import messages
import string 
import random 
media_url=settings.MEDIA_URL
curl=settings.CURRENT_URL
		
# user home page 
def home(request):
	dataa=add.objects.all()
	socialdata=Social_Links.objects.all()
	footerdata=footer_data.objects.all()
	BannerD=Banner_data.objects.all()

	return render(request,'basee.html',{'curl':curl,'dataa':dataa,'BannerD':BannerD,'socialdata':socialdata,'footerdata':footerdata})

# about us 
def about(request):
	socialdata=Social_Links.objects.all()
	footerdata=footer_data.objects.all()
	dataa=add.objects.all()
	return render(request,'about.html',{'curl':curl,'dataa':dataa,'socialdata':socialdata,'footerdata':footerdata})


# all blogs
def blog(request):
	cate_data=Add_category.objects.all()
	socialdata=Social_Links.objects.all()
	footerdata=footer_data.objects.all()
	blogData=admin_block.objects.all().order_by('-date')
	paginator=Paginator(blogData ,8)
	page=request.GET.get('page')
	# print(page)
	blogDat=paginator.get_page(page)
	# print(blogData)
	# try:
	# 	posts=paginator.page(page)
	# except PageNotAnInteger:
	# 	posts=paginator.page(1)
	# except EmptyPage:
	# 	posts=paginator.page(paginator.num_pages)

	return render(request,'blog.html',{'curl':curl,'blogDat':blogDat,'socialdata':socialdata,'footerdata':footerdata,'cate_data':cate_data})

# contact form 
def contact(request):
	N = 15
	res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
	if request.method =='POST':
		username=request.POST['username']
		email=request.POST['email']
		subject=request.POST['subject']
		description=request.POST['description']
		# date=request.POST['date']
		token=request.POST['token']
		# status=request.POST['status']
		a=models.user_enquiry(username=username,email=email,subject=subject,description=description,token=res)
		a.save()
	socialdata=Social_Links.objects.all()
	footerdata=footer_data.objects.all()
	contact_Data=contact_us.objects.all()

	return render(request,'contact_us.html',{'curl':curl,'contact_Data':contact_Data,'socialdata':socialdata,'footerdata':footerdata})

def handlelogout(request):
	logout(request)
	return redirect('/singup')
#this is for user login
@unauthenticated_user	
def Singin(request):
	socialdata=Social_Links.objects.all()
	footerdata=footer_data.objects.all()
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/my_project')
		else:
			return render(request,'singin.html',{'curl':curl,'socialdata':socialdata,'footerdata':footerdata})
	else:
		return render(request,'singin.html',{'curl':curl,'socialdata':socialdata,'footerdata':footerdata})

# Register form user Register
@unauthenticated_user
def Singup(request):
	if request.method=='POST':
		# import pdb;pdb.set_trace();
		form=CreateUserform(request.POST)
		profile_form=userprofileform(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			#profile=profile_form.save(commit=False)
			profile=user.userprofile
			#profile.user=user
			profile.Skills = profile_form.cleaned_data['Skills']
			profile.Experience = profile_form.cleaned_data['Experience']
			profile.collage = profile_form.cleaned_data['collage'] 
			profile.save()
			username=form.cleaned_data.get('username')
			group=Group.objects.get(name='customer')
			user.groups.add(group)
			messages.success(request,'Account was created for ' +username)
			return redirect('/singin')
	else:
		form=CreateUserform()
		profile_form=userprofileform()
	socialdata=Social_Links.objects.all()
	footerdata=footer_data.objects.all()
	return render(request,'singup2.html',{'curl':curl,'form':form,'profile_form':profile_form,'socialdata':socialdata,'footerdata':footerdata})

# blog id for search 
def blogid(request,category):
	cate_data=Add_category.objects.all()
	data=Add_category.objects.filter(category=category)
	
	socialdata=Social_Links.objects.all()
	footerdata=footer_data.objects.all()
	blogData=admin_block.objects.all()

	for cate in data:
		for blog in  blogData:
			if cate.category == blog.Select_Catogry:
				render(request,'nnnn.html',{'data':data,'curl':curl,'blogData':blogData,'socialdata':socialdata,'footerdata':footerdata,'cate_data':cate_data})
			else:
				return render(request,'nnnn.html',{'data':data,'curl':curl,'blogData':blogData,'socialdata':socialdata,'footerdata':footerdata,'cate_data':cate_data})

# jobs find
def brower_jobs(request):
	Post_jobs=Postjobs.objects.all().order_by('-Date')
	Assign=assignproject.objects.all()
	Post_jobcount=Postjobs.objects.all().count()
	footerdata=footer_data.objects.all()
	paginator=Paginator(Post_jobs ,6)
	page=request.GET.get('page')
	# print(page)
	postjob=paginator.get_page(page)
	return render(request,'browser_jobs.html',{'footerdata':footerdata,'Assign':Assign,'postjob':postjob,'curl':curl,'Post_jobs':Post_jobs,'Post_jobcount':Post_jobcount})

# this is for bussiness enquiry
def Bussines_enquiry(request):
	N = 15
	res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
	if request.method =='POST':
		company_name=request.POST['company_name']
		company_email=request.POST['company_email']
		company_subject=request.POST['company_subject']
		company_description=request.POST['company_description']
		company_contact=request.POST['company_contact']
		# date=request.POST['date']
		company_token=request.POST['company_token']
		# status=request.POST['status']
		a=models.business_enquire(company_contact=company_contact,company_name=company_name,company_email=company_email,company_subject=company_subject,company_description=company_description,company_token=res)
		a.save()
	Bus_Content=Bussines_content.objects.all()
	footerdata=footer_data.objects.all()
	return render(request,'Bussines_enquiry.html',{'footerdata':footerdata,'curl':curl,'Bus_Content':Bus_Content})

# show blog data and blog details 
def blog_details(request,id):
	blogData=admin_block.objects.filter(id=id)
	
	footerdata=footer_data.objects.all()
	return render(request,'blog_details.html',{'footerdata':footerdata,'curl':curl,'blogData':blogData})


### User profile
@login_required(login_url='/singin')
def my_profile(request):
	user_data=userprofile.objects.all()
	footerdata=footer_data.objects.all()
	return render(request,'Myprofile.html',{'curl':curl,'footerdata':footerdata,'user_data':user_data})

## User project
@login_required(login_url='/singin')	
def my_project(request):
	Post_jobs=Postjobs.objects.all().order_by('-Date')
	footerdata=footer_data.objects.all()
	assingpro=assignproject.objects.all()
	return render(request,'Myprojects.html',{'curl':curl,'footerdata':footerdata,'assingpro':assingpro,'Post_jobs':Post_jobs})

# gernal information 
@login_required(login_url='/singin')	
def genralinformation(request):
	user_data=userprofile.objects.all()
	footerdata=footer_data.objects.all()
	return render(request,'genral_information.html',{'curl':curl,'footerdata':footerdata,'user_data':user_data})
#edit user profile

@login_required(login_url='/singin')
def profileedit(request):
	footerdata=footer_data.objects.all()
	user_form=Userupdateform(request.POST,instance=request.user)
	user_profile=Userprofileupdateform(request.POST,instance=request.user.userprofile)
	if request.method=='POST':
		if user_form.is_valid() and user_profile.is_valid():
			user_form.save()
			user_profile.save()
			messages.success(request,'details update')
			return redirect('/my_profile')
	else:
		user_form=Userupdateform(instance=request.user)
		user_profile=Userprofileupdateform(instance=request.user.userprofile)
	return render(request,'profileedit.html',{'curl':curl,'user_form':user_form,'user_profile':user_profile,'footerdata':footerdata})

### This is for apply for project ###
@login_required(login_url='/singin')
def apply(request,id):
	Post_jobs=Postjobs.objects.all()
	Post_jobs=Postjobs.objects.filter(id=id)
	footerdata=footer_data.objects.all()
	if request.method=='POST':
		assignuser=request.POST.get('assignuser')
		assignproject=request.POST.get('assignproject')
		amount=request.POST.get('amount')
		ProjectName=request.POST.get('ProjectName')
		Companyname=request.POST.get('Companyname')
		skills=request.POST.get('skills')
		Description=request.POST.get('Description')
		Duration=request.POST.get('Duration')
		userassign=models.assignproject(Duration=Duration,assignuser=assignuser,assignproject=assignproject,amount=amount,ProjectName=ProjectName,Companyname=Companyname,skills=skills,Description=Description)
		userassign.save()
		return redirect('/my_project')
	return render(request,'apply.html',{'curl':curl,'Post_jobs':Post_jobs,'footerdata':footerdata})

@login_required(login_url='/singin')
def assignDelete(request,id):


	assign_del=assignproject.objects.filter(id=id)
	assign_del.delete()
	return redirect('/my_project')

def paymentpage(request):
	footerdata=footer_data.objects.all()
	return render(request,'paymentpage.html',{'curl':curl,'footerdata':footerdata})