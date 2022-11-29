from django.shortcuts import render ,redirect
from django.http import HttpResponse
from Recruitmentadmin.models import *
from Recruitmentadmin.models import Postjobs
from django.conf import settings
from .models import *
from django.core.files.storage import FileSystemStorage
from .models import user_enquiry 
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger
from .import models
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User ,auth
from .forms import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
from datetime import date
import string 
import random 
media_url=settings.MEDIA_URL
curl=settings.CURRENT_URL
from .smsapi import *

		
# user home pa ge 
def home(request):
	

	return render(request,'basee.html')



def flag_details(request):
	if FlagDetail.objects.select_related('user').filter(user=request.user,personal_detail_flag=True,other_detail_flag=False,education_details_flag=False,address_detail_flag=False,
								bank_detail_flag=False,document_upload_flag=False,choice_filling_flag=False,payment_flag=False,final_submit_flag=False):
		return redirect("/other/details/")
	elif FlagDetail.objects.select_related('user').filter(user=request.user,personal_detail_flag=True,other_detail_flag=True,education_details_flag=False,address_detail_flag=False,
								bank_detail_flag=False,document_upload_flag=False,choice_filling_flag=False,payment_flag=False,final_submit_flag=False):
		return redirect("/education/details/")
	elif FlagDetail.objects.select_related('user').filter(user=request.user,personal_detail_flag=True,other_detail_flag=True,education_details_flag=True,address_detail_flag=False,
								bank_detail_flag=False,document_upload_flag=False,choice_filling_flag=False,payment_flag=False,final_submit_flag=False):
		return redirect("/address/details/")

	elif FlagDetail.objects.select_related('user').filter(user=request.user,personal_detail_flag=True,other_detail_flag=True,education_details_flag=True,address_detail_flag=True,
								bank_detail_flag=False,document_upload_flag=False,choice_filling_flag=False,payment_flag=False,final_submit_flag=False):
		return redirect("/bank/details/")
	elif FlagDetail.objects.select_related('user').filter(user=request.user,personal_detail_flag=True,other_detail_flag=True,education_details_flag=True,address_detail_flag=True,
								bank_detail_flag=True,document_upload_flag=False,choice_filling_flag=False,payment_flag=False,final_submit_flag=False):
		return redirect("/document/upload/")
	elif FlagDetail.objects.select_related('user').filter(user=request.user,personal_detail_flag=True,other_detail_flag=True,education_details_flag=True,address_detail_flag=True,
								bank_detail_flag=True,document_upload_flag=True,choice_filling_flag=False,payment_flag=False,final_submit_flag=False):
		return redirect("/choice/filling/")
	elif FlagDetail.objects.select_related('user').filter(user=request.user,personal_detail_flag=True,other_detail_flag=True,education_details_flag=True,address_detail_flag=True,
								bank_detail_flag=True,document_upload_flag=True,choice_filling_flag=True,payment_flag=False,final_submit_flag=False):
		return redirect("/Final_Submit/")
	elif FlagDetail.objects.select_related('user').filter(user=request.user,personal_detail_flag=True,other_detail_flag=True,education_details_flag=True,address_detail_flag=True,
								bank_detail_flag=True,document_upload_flag=True,choice_filling_flag=True,payment_flag=False,final_submit_flag=True):
		return redirect("/pdf/")
	else:
		return redirect('/Candidate_declaration')

 
# all blogs

# contact form 
# def contact(request):
# 	N = 15
# 	res = ''.join(random.choices(string.ascii_uppercase +
#                              string.digits, k = N))
# 	if request.method =='POST':
# 		username=request.POST['username']
# 		email=request.POST['email']
# 		subject=request.POST['subject']
# 		description=request.POST['description']
# 		# date=request.POST['date']
# 		token=request.POST['token']
# 		# status=request.POST['status']
# 		a=models.user_enquiry(username=username,email=email,subject=subject,description=description,token=res)
# 		a.save()
# 	socialdata=Social_Links.objects.all()
# 	footerdata=footer_data.objects.all()
# 	contact_Data=contact_us.objects.all()

# 	return render(request,'contact_us.html',{'curl':curl,'contact_Data':contact_Data,'socialdata':socialdata,'footerdata':footerdata})

def handlelogout(request):
	logout(request)
	return redirect('/singin')
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
			return redirect('/Apply')
		else:
			message=messages.error(request,'Please Check  User Name And Password')
			return render(request,'singin.html',{'curl':curl,'socialdata':socialdata,'footerdata':footerdata,'message':message})
	else:
		return render(request,'singin.html',{'curl':curl,'socialdata':socialdata,'footerdata':footerdata})
 
# Register form user Register
@unauthenticated_user
def Singup(request):
	if request.method=='POST':
		form=CreateUserform(request.POST)
		profile_form=userprofileform(request.POST)
		if form.is_valid() and profile_form.is_valid():
			user=form.save()
			
			profile=user.userprofile
			
			
			profile.phone= profile_form.cleaned_data['phone']
			
			profile.save()
			username=form.cleaned_data.get('username')
			Name = form.cleaned_data.get('firstname')
			Mobile =form.cleaned_data.get('phone')
			group=Group.objects.get(name='applicant')
			user.groups.add(group)
			Temp_id=1007920182565424693
			sms_data(profile.phone,Temp_id,Name)
			messages.success(request,'Account Has Been Created for ' +username)
			return redirect('/singin')
	else:
		form=CreateUserform()
		profile_form=userprofileform()
	
	return render(request,'singup2.html',{'curl':curl,'form':form,'profile_form':profile_form})

# this is for bussiness enquiry
	# N = 15
	# res = ''.join(random.choices(string.ascii_uppercase +
 #                             string.digits, k = N))

 # this is for personal_details------------------------------
@login_required(login_url='/singin')	
def personal_details(request):
	if PersonalDetail.objects.filter(USER_CODE=request.user).exists():
		if request.method == 'POST':
			Departmental_Candidate = request.POST.get('switch-one')
			Employment_Type = request.POST.get('Employment_Type')
			Posted_Since = request.POST.get('Posted_Since')
			Gate_Score_Year = request.POST.get('Gate_Score_Year')
			Gate_Score = request.POST.get('Gate_Score')
			Gate_Roll_No = request.POST.get('Gate_Roll')
			select_Position = request.POST.get('select_Position')
			Aadhaar_Card_No = request.POST.get('Aadhaar_Card_No')
			Fisrt_Name = request.POST.get('Fisrt_Name')
			Middle_Name = request.POST.get('Middle_Name')
			Last_Name = request.POST.get('Last_Name')
			Father_Name = request.POST.get('Father_Name')
			Mother_Name = request.POST.get('Mother_Name')
			Date_Of_Birth = request.POST.get('Date_Of_Birth') 
			gender = request.POST.get('switch-gender')
			
			
			data = PersonalDetail.objects.filter(USER_CODE=request.user).update(IS_APPLICANT_A_DEPARTMENTAL_CANDIDATE = Departmental_Candidate,

									EMPLOYMENT_TYPE = Employment_Type,POSTED_SINCE=Posted_Since,GATE_SCORE_YEAR = 
									Gate_Score_Year,GATE_SCORE = Gate_Score,GATE_ROLL_NO = Gate_Roll_No,POST_APPLIED_FOR = select_Position,
									AADHAAR_CARD_NO = Aadhaar_Card_No,FIRST_NAME = Fisrt_Name,MIDDLE_NAME = 
									Middle_Name,LAST_NAME = Last_Name,FATHER_NAME = Father_Name,MOTHER_NAME = Mother_Name
									,DATE_OF_BIRTH = Date_Of_Birth,CANDIDATE_GENDER = gender, USER_CODE = request.user

									)
			return redirect('/other/details/')

		else:

			personal_data = PersonalDetail.objects.get(USER_CODE=request.user)
			return render(request,'personal_details.html',{'personal_data':personal_data})
	else:
		if request.method == 'POST':
			Departmental_Candidate = request.POST.get('switch-one')
			Employment_Type = request.POST.get('Employment_Type')
			Posted_Since = request.POST.get('Posted_Since')
			Gate_Score_Year = request.POST.get('Gate_Score_Year')
			Gate_Score = request.POST.get('Gate_Score')
			Gate_Roll_No = request.POST.get('Gate_Roll')
			select_Position = request.POST.get('select_Position')
			Aadhaar_Card_No = request.POST.get('Aadhaar_Card_No')
			Fisrt_Name = request.POST.get('Fisrt_Name')
			Middle_Name = request.POST.get('Middle_Name')
			Last_Name = request.POST.get('Last_Name')
			Father_Name = request.POST.get('Father_Name')
			Mother_Name = request.POST.get('Mother_Name')
			Date_Of_Birth = request.POST.get('Date_Of_Birth') 
			gender = request.POST.get('switch-gender')
			
			
			data = PersonalDetail(IS_APPLICANT_A_DEPARTMENTAL_CANDIDATE = Departmental_Candidate,
									EMPLOYMENT_TYPE = Employment_Type,POSTED_SINCE=Posted_Since,GATE_SCORE_YEAR = 
									Gate_Score_Year,GATE_SCORE = Gate_Score,GATE_ROLL_NO = Gate_Roll_No,POST_APPLIED_FOR = select_Position,
									AADHAAR_CARD_NO = Aadhaar_Card_No,FIRST_NAME = Fisrt_Name,MIDDLE_NAME = 
									Middle_Name,LAST_NAME = Last_Name,FATHER_NAME = Father_Name,MOTHER_NAME = Mother_Name
									,DATE_OF_BIRTH = Date_Of_Birth,CANDIDATE_GENDER = gender, USER_CODE = request.user

									)
			data.save()
			if  FlagDetail.objects.select_related('user').filter(user=request.user).exists():
				Flag_data = FlagDetail.objects.get(user=request.user)
				Flag_data.personal_detail_flag=1
				Flag_data.save()
			else:
				Flag_data = FlagDetail(personal_detail_flag=1,user=request.user)
				Flag_data.save()


			return redirect('/other/details/')

		else:
			return render(request,'personal_details.html')

# end personl details

# start other details
@login_required(login_url='/singin')	
def other_details(request):
	Date_Of_Birth_of_user = PersonalDetail.objects.get(USER_CODE=request.user)
	if OtherDetail.objects.filter(USER_CODE=request.user).exists():
		try:
			if request.method == "POST":
				married = request.POST.get('switch-married')
				H_W_Name = request.POST.get('H-W_Name')
				Total_Child = request.POST.get('Total_Child')
				Child_Dob = request.POST.get('Child_Dob')
				Twin = request.POST.get('switch-twin')
				Divorced = request.POST.get('switch-divorced')
				Country_native = request.POST.get('country')
				NATIVE_OF_MADHYA_PRADESH = request.POST.get('switch-one')
				CATEGORY = request.POST.get('switch-two')
				BELONGS_TO_CREAMY_LAYER = request.POST.get('switch-CREAMY')
				DISABILITY_CERTIFICATE = request.POST.get('switch-CERTIFICATE')
				MINIMUM_40_PERCENT_DISABILITY = request.POST.get('switch-PERCENT')
				TYPE_OF_DISABILITY = request.POST.get('type-of-disability')
				PERCENTAGE_OF_DISABILITY = request.POST.get('Percentage-of-Disability')
				CANDIDATE_PUNISHED = request.POST.get('switch-PUNISHED')
				DEBARRED_PERIOD_FROM_ANY_EXAMINATION = request.POST.get('switch-SELECTION')
				SERVING_IN_THE_GOVERNMENT = request.POST.get('switch-SERVING')
				LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE = request.POST.get('switch-LIVEREGISTRATION')
				INTER_CASTE_MARRIAGE = request.POST.get('switch-Department')
				VIKRAM_AWARDEE_SPORTSPERSON = request.POST.get('switch-Vikram')
				EX_SERVICEMAN = request.POST.get('switch-EX-SERVICEMAN')
				PERIOD_OF_SERVICE = request.POST.get('Service_Period')
				data = OtherDetail.objects.filter(USER_CODE=request.user).update(
					USER_CODE = request.user,
					IS_CANDIDATES_MARRIED = married,HUSBAND_WIFE_NAME = H_W_Name,NUMBER_OF_SURVIVING_CHILDREN = Total_Child,
					LAST_CHILD_DATE_OF_BIRTH = Child_Dob,IS_THE_LAST_CHILD_TWIN = Twin,
					CANDIDATE_IS_A_WIDOW_DIVORCED_ABANDONED_WOMAN = Divorced,COUNTRY=Country_native,NATIVE_OF_MADHYA_PRADESH = NATIVE_OF_MADHYA_PRADESH,CATEGORY = CATEGORY,
					   BELONGS_TO_CREAMY_LAYER = BELONGS_TO_CREAMY_LAYER,DISABILITY_CERTIFICATE = DISABILITY_CERTIFICATE,
					   MINIMUM_40_PERCENT_DISABILITY = MINIMUM_40_PERCENT_DISABILITY,TYPE_OF_DISABILITY = TYPE_OF_DISABILITY,
					   PERCENTAGE_OF_DISABILITY = PERCENTAGE_OF_DISABILITY,CANDIDATE_PUNISHED = CANDIDATE_PUNISHED,
					   DEBARRED_PERIOD_FROM_ANY_EXAMINATION = DEBARRED_PERIOD_FROM_ANY_EXAMINATION,SERVING_IN_THE_GOVERNMENT 
					   = SERVING_IN_THE_GOVERNMENT,LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE = LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE
					   ,INTER_CASTE_MARRIAGE = INTER_CASTE_MARRIAGE,VIKRAM_AWARDEE_SPORTSPERSON = VIKRAM_AWARDEE_SPORTSPERSON,
					   EX_SERVICEMAN=EX_SERVICEMAN,PERIOD_OF_SERVICE=PERIOD_OF_SERVICE
					   )
				return redirect('/education/details/')
			else:
				other_data = OtherDetail.objects.get(USER_CODE=request.user)
				return render(request,'other_details.html',{'other_data':other_data,'DOB':Date_Of_Birth_of_user})
		except Exception as e:
			return HttpResponse(e)
	else:
		if request.method == "POST":
			married = request.POST.get('switch-married')
			H_W_Name = request.POST.get('H-W_Name' or None)
			Total_Child = request.POST.get('Total_Child')
			Child_Dob = request.POST.get('Child_Dob')
			Twin = request.POST.get('switch-twin')
			Divorced = request.POST.get('switch-divorced')
			Country = request.POST.get('country')
			NATIVE_OF_MADHYA_PRADESH = request.POST.get('switch-one')
			CATEGORY = request.POST.get('switch-two')
			BELONGS_TO_CREAMY_LAYER = request.POST.get('switch-CREAMY')
			DISABILITY_CERTIFICATE = request.POST.get('switch-CERTIFICATE')
			MINIMUM_40_PERCENT_DISABILITY = request.POST.get('switch-PERCENT')
			TYPE_OF_DISABILITY = request.POST.get('type-of-disability')
			PERCENTAGE_OF_DISABILITY = request.POST.get('Percentage-of-Disability')
			CANDIDATE_PUNISHED = request.POST.get('switch-PUNISHED')
			DEBARRED_PERIOD_FROM_ANY_EXAMINATION = request.POST.get('switch-SELECTION')
			SERVING_IN_THE_GOVERNMENT = request.POST.get('switch-SERVING')
			LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE = request.POST.get('switch-LIVEREGISTRATION')
			INTER_CASTE_MARRIAGE = request.POST.get('switch-Department')
			VIKRAM_AWARDEE_SPORTSPERSON = request.POST.get('switch-Vikram')
			EX_SERVICEMAN = request.POST.get('switch-EX-SERVICEMAN')
			PERIOD_OF_SERVICE = request.POST.get('Service_Period')
			data = OtherDetail(
				USER_CODE = request.user,
				IS_CANDIDATES_MARRIED = married,HUSBAND_WIFE_NAME = H_W_Name,NUMBER_OF_SURVIVING_CHILDREN = Total_Child,
				LAST_CHILD_DATE_OF_BIRTH = Child_Dob,IS_THE_LAST_CHILD_TWIN = Twin,
				CANDIDATE_IS_A_WIDOW_DIVORCED_ABANDONED_WOMAN = Divorced,COUNTRY=Country,NATIVE_OF_MADHYA_PRADESH = NATIVE_OF_MADHYA_PRADESH,CATEGORY = CATEGORY,
				BELONGS_TO_CREAMY_LAYER = BELONGS_TO_CREAMY_LAYER,DISABILITY_CERTIFICATE = DISABILITY_CERTIFICATE,
				MINIMUM_40_PERCENT_DISABILITY = MINIMUM_40_PERCENT_DISABILITY,TYPE_OF_DISABILITY = TYPE_OF_DISABILITY,
				PERCENTAGE_OF_DISABILITY = PERCENTAGE_OF_DISABILITY,CANDIDATE_PUNISHED = CANDIDATE_PUNISHED,
				DEBARRED_PERIOD_FROM_ANY_EXAMINATION = DEBARRED_PERIOD_FROM_ANY_EXAMINATION,SERVING_IN_THE_GOVERNMENT 
				= SERVING_IN_THE_GOVERNMENT,LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE = LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE
				,INTER_CASTE_MARRIAGE = INTER_CASTE_MARRIAGE,VIKRAM_AWARDEE_SPORTSPERSON = VIKRAM_AWARDEE_SPORTSPERSON,
				EX_SERVICEMAN=EX_SERVICEMAN,PERIOD_OF_SERVICE=PERIOD_OF_SERVICE
				)
			data.save()
			if  FlagDetail.objects.select_related('user').filter(user=request.user).exists():
				Flag_data = FlagDetail.objects.get(user=request.user)
				Flag_data.other_detail_flag=1
				Flag_data.save()
			else:
				Flag_data = FlagDetail(other_detail_flag=1,user=request.user)
				Flag_data.save()
			return redirect('/education/details/')
		else:
			return render(request,'other_details.html',{'DOB':Date_Of_Birth_of_user})

# end other details

#start education details
@login_required(login_url='/singin')	
def education_details(request):
	Date_Of_Birth_of_user = PersonalDetail.objects.get(USER_CODE=request.user)
	if EducationDetails.objects.filter(USER_CODE=request.user).exists():

		if request.method == "POST":
			HSC_SUBJECT = request.POST['HSC_SUBJECT']
			HSC_PERCENTAGE = request.POST['HSC_PERCENTAGE']
			HSC_PASSING_YEAR = request.POST['HSC_PASSING_YEAR']
			HSSC_SUBJECT = request.POST['HSSC_SUBJECT']
			HSSC_PERCENTAGE = request.POST['HSSC_PERCENTAGE']
			HSSC_PASSING_YEAR = request.POST['HSSC_PASSING_YEAR']
			GRADUATION_SUBJECT = request.POST['GRADUATION_SUBJECT']
			GRADUATION_PERCENTAGE = request.POST['GRADUATION_PERCENTAGE']
			GRADUATION_PASSING_YEAR = request.POST['GRADUATION_PASSING_YEAR']
			POST_GRADUATION_SUBJECT = request.POST['POST_GRADUATION_SUBJECT']
			POST_GRADUATION_PERCENTAGE = request.POST['POST_GRADUATION_PERCENTAGE']
			POST_PASSING_YEAR = request.POST['POST_PASSING_YEAR']
			data = EducationDetails.objects.filter(USER_CODE=request.user).update(
					USER_CODE=request.user,HSC_SUBJECT = HSC_SUBJECT,HSC_PERCENTAGE = HSC_PERCENTAGE,
					HSC_PASSING_YEAR = HSC_PASSING_YEAR,HSSC_SUBJECT = HSSC_SUBJECT,HSSC_PERCENTAGE = HSSC_PERCENTAGE,
					HSSC_PASSING_YEAR = HSSC_PASSING_YEAR,GRADUATION_SUBJECT = GRADUATION_SUBJECT,GRADUATION_PERCENTAGE
					= GRADUATION_PERCENTAGE,GRADUATION_PASSING_YEAR = GRADUATION_PASSING_YEAR,POST_GRADUATION_SUBJECT = 
					POST_GRADUATION_SUBJECT,POST_GRADUATION_PERCENTAGE = POST_GRADUATION_PERCENTAGE,POST_PASSING_YEAR = 
					POST_PASSING_YEAR
					)
			return redirect('/address/details/')
		else:
			Education_Data = EducationDetails.objects.get(USER_CODE=request.user)
			return render(request,'education_details.html',{'Education_Data':Education_Data,'DOB':Date_Of_Birth_of_user})
	else:
		if request.method == "POST":
			HSC_SUBJECT = request.POST['HSC_SUBJECT']
			HSC_PERCENTAGE = request.POST['HSC_PERCENTAGE']
			HSC_PASSING_YEAR = request.POST['HSC_PASSING_YEAR']
			HSSC_SUBJECT = request.POST['HSSC_SUBJECT']
			HSSC_PERCENTAGE = request.POST['HSSC_PERCENTAGE']
			HSSC_PASSING_YEAR = request.POST['HSSC_PASSING_YEAR']
			GRADUATION_SUBJECT = request.POST['GRADUATION_SUBJECT']
			GRADUATION_PERCENTAGE = request.POST['GRADUATION_PERCENTAGE']
			GRADUATION_PASSING_YEAR = request.POST['GRADUATION_PASSING_YEAR']
			POST_GRADUATION_SUBJECT = request.POST['POST_GRADUATION_SUBJECT']
			POST_GRADUATION_PERCENTAGE = request.POST['POST_GRADUATION_PERCENTAGE']
			POST_PASSING_YEAR = request.POST['POST_PASSING_YEAR']
			data = EducationDetails(
					USER_CODE=request.user,HSC_SUBJECT = HSC_SUBJECT,HSC_PERCENTAGE = HSC_PERCENTAGE,
					HSC_PASSING_YEAR = HSC_PASSING_YEAR,HSSC_SUBJECT = HSSC_SUBJECT,HSSC_PERCENTAGE = HSSC_PERCENTAGE,
					HSSC_PASSING_YEAR = HSSC_PASSING_YEAR,GRADUATION_SUBJECT = GRADUATION_SUBJECT,GRADUATION_PERCENTAGE
					= GRADUATION_PERCENTAGE,GRADUATION_PASSING_YEAR = GRADUATION_PASSING_YEAR,POST_GRADUATION_SUBJECT = 
					POST_GRADUATION_SUBJECT,POST_GRADUATION_PERCENTAGE = POST_GRADUATION_PERCENTAGE,POST_PASSING_YEAR = 
					POST_PASSING_YEAR
					)
			data.save()
			if  FlagDetail.objects.select_related('user').filter(user=request.user).exists():
				Flag_data = FlagDetail.objects.get(user=request.user)
				Flag_data.education_details_flag=1
				Flag_data.save()
			else:
				Flag_data = FlagDetail(education_details_flag=1,user=request.user)
				Flag_data.save()
			return redirect('/address/details/')
		else:
			return render(request,'education_details.html',{'DOB':Date_Of_Birth_of_user})

# end education 

# start Address code
@login_required(login_url='/singin')	
def address(request):
	if AddressDetail.objects.filter(USER_CODE=request.user).exists():
		if request.method == "POST":
			PRESENT_STATE = request.POST['Present_State']
			PRESENT_DISTRICT = request.POST['Present_District']
			PRESENT_PIN_CODE = request.POST['Present_Pin']
			PRESENT_LAND_MARK = request.POST['Present_Land_Mark']
			MOBILE_NUMBER = request.POST['Mobile_number']
			EMAIL_ID = request.POST['Email_Id']
			PRESENT_ADDRESS = request.POST['Present_Address']
			PERMANENT_STATE = request.POST['Permanent_State']
			PERMANENT_DISTRICT = request.POST['Permanent_District']
			PERMANENT_PIN_CODE = request.POST['Permanent_Pin_Code']
			PERMANENT_LAND_MARK = request.POST['Permanent_Land_Mark']
			PERMANENT_ADDRESS = request.POST['Permanent_Address']
			data = AddressDetail.objects.filter(USER_CODE=request.user).update(
					USER_CODE = request.user,
					PRESENT_STATE = PRESENT_STATE,PRESENT_DISTRICT = PRESENT_DISTRICT,PRESENT_PIN_CODE = PRESENT_PIN_CODE,
					PRESENT_LAND_MARK = PRESENT_LAND_MARK,MOBILE_NUMBER = MOBILE_NUMBER,EMAIL_ID = EMAIL_ID,PRESENT_ADDRESS
					= PRESENT_ADDRESS,PERMANENT_DISTRICT = PERMANENT_DISTRICT,PERMANENT_PIN_CODE = PERMANENT_PIN_CODE,
					PERMANENT_LAND_MARK = PERMANENT_LAND_MARK,PERMANENT_ADDRESS = PERMANENT_ADDRESS
					)
			return redirect('/bank/details/')
		else:
			Address_Data = AddressDetail.objects.get(USER_CODE=request.user)
			return render(request,'address.html',{'Address_Data':Address_Data})
	else:
		if request.method == "POST":
			PRESENT_STATE = request.POST['Present_State']
			PRESENT_DISTRICT = request.POST['Present_District']
			PRESENT_PIN_CODE = request.POST['Present_Pin']
			PRESENT_LAND_MARK = request.POST['Present_Land_Mark']
			MOBILE_NUMBER = request.POST['Mobile_number']
			EMAIL_ID = request.POST['Email_Id']
			PRESENT_ADDRESS = request.POST['Present_Address']
			PERMANENT_STATE = request.POST['Permanent_State']
			PERMANENT_DISTRICT = request.POST['Permanent_District']
			PERMANENT_PIN_CODE = request.POST['Permanent_Pin_Code']
			PERMANENT_LAND_MARK = request.POST['Permanent_Land_Mark']
			PERMANENT_ADDRESS = request.POST['Permanent_Address']
			data = AddressDetail(
					USER_CODE = request.user,
					PRESENT_STATE = PRESENT_STATE,PRESENT_DISTRICT = PRESENT_DISTRICT,PRESENT_PIN_CODE = PRESENT_PIN_CODE,
					PRESENT_LAND_MARK = PRESENT_LAND_MARK,MOBILE_NUMBER = MOBILE_NUMBER,EMAIL_ID = EMAIL_ID,PRESENT_ADDRESS
					= PRESENT_ADDRESS,PERMANENT_DISTRICT = PERMANENT_DISTRICT,PERMANENT_PIN_CODE = PERMANENT_PIN_CODE,
					PERMANENT_LAND_MARK = PERMANENT_LAND_MARK,PERMANENT_ADDRESS = PERMANENT_ADDRESS
					)
			data.save()
			if  FlagDetail.objects.select_related('user').filter(user=request.user).exists():
				Flag_data = FlagDetail.objects.get(user=request.user)
				Flag_data.address_detail_flag=1
				Flag_data.save()
			else:
				Flag_data = FlagDetail(address_detail_flag=1,user=request.user)
				Flag_data.save()
			return redirect('/bank/details/')
		else:
			return render(request,'address.html')

# end address code
# start bank details
@login_required(login_url='/singin')	
def bank_details(request):
	if BankDetail.objects.filter(USER_CODE=request.user).exists():
		if request.method == "POST":
			BANK_NAME = request.POST['Bank_Name']
			IFSC_CODE = request.POST['Isfc_code']
			BRANCH_NAME = request.POST['Branch_Name']
			BRANCH_CODE = request.POST['Branch_Code']
			ACCOUNT_HOLDER_NAME = request.POST['Account']
			ACCOUNT_NUMBER = request.POST['company_name']
			data = BankDetail.objects.filter(USER_CODE=request.user).update(
				USER_CODE=request.user,
				BANK_NAME = BANK_NAME,IFSC_CODE = IFSC_CODE,BRANCH_NAME = BRANCH_NAME,
				BRANCH_CODE = BRANCH_CODE,ACCOUNT_HOLDER_NAME = ACCOUNT_HOLDER_NAME,ACCOUNT_NUMBER = ACCOUNT_NUMBER)
			return redirect('/document/upload/')
		else:
			Bank_Data = BankDetail.objects.get(USER_CODE=request.user)
			return render(request,'bank_details.html',{'Bank_Data':Bank_Data})

	else:
		if request.method == "POST":
			BANK_NAME = request.POST['Bank_Name']
			IFSC_CODE = request.POST['Isfc_code']
			BRANCH_NAME = request.POST['Branch_Name']
			BRANCH_CODE = request.POST['Branch_Code']
			ACCOUNT_HOLDER_NAME = request.POST['Account']
			ACCOUNT_NUMBER = request.POST['company_name']
			data = BankDetail(
				USER_CODE=request.user,
				BANK_NAME = BANK_NAME,IFSC_CODE = IFSC_CODE,BRANCH_NAME = BRANCH_NAME,
				BRANCH_CODE = BRANCH_CODE,ACCOUNT_HOLDER_NAME = ACCOUNT_HOLDER_NAME,ACCOUNT_NUMBER = ACCOUNT_NUMBER)
			data.save()
			if  FlagDetail.objects.select_related('user').filter(user=request.user).exists():
				Flag_data = FlagDetail.objects.get(user=request.user)
				Flag_data.bank_detail_flag=1
				Flag_data.save()
			else:
				Flag_data = FlagDetail(bank_detail_flag=1,user=request.user)
				Flag_data.save()
			return redirect('/document/upload/')
		else:
			return render(request,'bank_details.html')
#end bankdetails
# document upload 
@login_required(login_url='/singin')
def document_upload(request):
	
	if request.method == "POST":
		HIGH_SCHOOL = request.FILES.get('HIGH_SCHOOL',None)
		HSSC = request.FILES.get('HSSC',None)
		GRADUATION_MARKSHEET = request.FILES.get('GRADUATION_MARKSHEET_PDF',None)
		POST_GRADUATION = request.FILES.get('POST_GRADUATION',None)
		AADHAAR_CARD = request.FILES.get('AADHAAR_CARD',None)
		CAST_CERTIFICATE = request.FILES.get('CAST_CERTIFICATE',None)
		GATE_SCORECARD = request.FILES.get('GATE_SCORECARD',None)
		DEPARTMENTAL_NOC = request.FILES.get('DEPARTMENTAL_NOC',None)
		Income_Certificate = request.FILES.get('Income_Certificate',None)
		Disabilty_Certficate = request.FILES.get('Disabilty_Certficate',None)
		if DocumentUpload.objects.filter(USER_CODE=request.user).exists():
			data = DocumentUpload.objects.filter(USER_CODE=request.user).update(USER_CODE=request.user,
									HIGH_SCHOOL = HIGH_SCHOOL,HSSC = HSSC,GRADUATION_MARKSHEET = GRADUATION_MARKSHEET,
									POST_GRADUATION = POST_GRADUATION,AADHAAR_CARD = AADHAAR_CARD,CAST_CERTIFICATE = 
									CAST_CERTIFICATE,GATE_SCORECARD = GATE_SCORECARD,DEPARTMENTAL_NOC = DEPARTMENTAL_NOC,
									INCOME_CERTIFICATE = Income_Certificate,DISABLITY_CERTIFICATE = Disabilty_Certficate
								)
			return redirect('/choice/filling/')
		else:
			data = DocumentUpload(
									USER_CODE=request.user,
									HIGH_SCHOOL = HIGH_SCHOOL,HSSC = HSSC,GRADUATION_MARKSHEET = GRADUATION_MARKSHEET,
									POST_GRADUATION = POST_GRADUATION,AADHAAR_CARD = AADHAAR_CARD,CAST_CERTIFICATE = 
									CAST_CERTIFICATE,GATE_SCORECARD = GATE_SCORECARD,DEPARTMENTAL_NOC = DEPARTMENTAL_NOC,
									INCOME_CERTIFICATE = Income_Certificate,DISABLITY_CERTIFICATE = Disabilty_Certficate
								)
			data.save()
			if  FlagDetail.objects.select_related('user').filter(user=request.user).exists():
				Flag_data = FlagDetail.objects.get(user=request.user)
				Flag_data.document_upload_flag=1
				Flag_data.save()
			else:
				Flag_data = FlagDetail(document_upload_flag=1,user=request.user)
				Flag_data.save()
			return redirect('/choice/filling/')

		
	else:
		return render(request,'document_upload.html')

# end upload document 
@login_required(login_url='/singin')
def choice_filling(request):
	
	Add_Vacancy_Position = AddVacancyPosition.objects.all()
	personal_value = PersonalDetail.objects.get(USER_CODE=request.user)
	other_value = OtherDetail.objects.get(USER_CODE=request.user)
	if ChoiceFilling.objects.filter(USER_CODE=request.user).exists():
		if request.method == "POST":
			CHOICE_11 = request.POST.get('Choice_1')
			CHOICE_22 = request.POST.get('Choice_2')
			CHOICE_33 = request.POST.get('Choice_3')
			CHOICE_44 = request.POST.get('Choice_4')
			CHOICE_55 = request.POST.get('Choice_5')
			CHOICE_66 = request.POST.get('Choice_6')
			print("hello")
			
			data = ChoiceFilling.objects.filter(USER_CODE=request.user).update(
					USER_CODE = request.user,
					CHOICE_1 = CHOICE_11,CHOICE_2 = CHOICE_22,CHOICE_3 = CHOICE_33,CHOICE_4 = CHOICE_44
					,CHOICE_5 = CHOICE_55,CHOICE_6=CHOICE_66)
			return redirect('/Final_Submit/')
		else:
			return render(request,'choice_filling.html',{'personal_value':personal_value,'other_value':other_value,'Add_Vacancy_Position':Add_Vacancy_Position})
	else:
		if request.method == "POST":
			CHOICE_11 = request.POST.get('Choice_1')
			CHOICE_22 = request.POST.get('Choice_2')
			CHOICE_33 = request.POST.get('Choice_3')
			CHOICE_44 = request.POST.get('Choice_4')
			CHOICE_55 = request.POST.get('Choice_5')
			CHOICE_66 = request.POST.get('Choice_6')
			print("---------------------------------",CHOICE_11)
			
			data = ChoiceFilling(
					USER_CODE = request.user,
					CHOICE_1 = CHOICE_11,CHOICE_2 = CHOICE_22,CHOICE_3 = CHOICE_33,CHOICE_4 = CHOICE_44
					,CHOICE_5 = CHOICE_55,CHOICE_6=CHOICE_66)
			data.save()
			if  FlagDetail.objects.select_related('user').filter(user=request.user).exists():
				Flag_data = FlagDetail.objects.get(user=request.user)
				Flag_data.choice_filling_flag=1
				Flag_data.save()
			else:
				Flag_data = FlagDetail(choice_filling_flag=1,user=request.user)
				Flag_data.save()
			return redirect('/Final_Submit/')
			
		else:
			return render(request,'choice_filling.html',{'personal_value':personal_value,'other_value':other_value,'Add_Vacancy_Position':Add_Vacancy_Position})

from itertools import chain
@login_required(login_url='/singin')
def Final_Submit(request):
	if FinalDataTable.objects.filter(USER_CODE=request.user).exists():
		return HttpResponse("data is already exits")
	else:
		data = PersonalDetail.objects.get(USER_CODE=request.user)
		other_value = OtherDetail.objects.get(USER_CODE=request.user)

		if request.method =="POST":
			data = PersonalDetail.objects.get(USER_CODE=request.user)
			data_2 = OtherDetail.objects.get(USER_CODE=request.user)
			data_3 = EducationDetails.objects.get(USER_CODE=request.user)
			data_4 = AddressDetail.objects.get(USER_CODE=request.user)
			data_5 = BankDetail.objects.get(USER_CODE=request.user)
			data_6 = DocumentUpload.objects.get(USER_CODE=request.user)
			data_7 = ChoiceFilling.objects.get(USER_CODE=request.user)
			submit_data = FinalDataTable(
						USER_CODE = request.user,
						IS_APPLICANT_A_DEPARTMENTAL_CANDIDATE = data.IS_APPLICANT_A_DEPARTMENTAL_CANDIDATE,EMPLOYMENT_TYPE=data.EMPLOYMENT_TYPE,POSTED_SINCE=data.POSTED_SINCE,
						GATE_SCORE_YEAR = data.GATE_SCORE_YEAR,
						GATE_SCORE = data.GATE_SCORE,GATE_ROLL_NO = data.GATE_ROLL_NO,AADHAAR_CARD_NO = data.AADHAAR_CARD_NO,
						FIRST_NAME = data.FIRST_NAME,MIDDLE_NAME = data.MIDDLE_NAME,LAST_NAME = data.LAST_NAME,FATHER_NAME = data.FATHER_NAME,
						MOTHER_NAME = data.MOTHER_NAME,DATE_OF_BIRTH = data.DATE_OF_BIRTH,CANDIDATE_GENDER = data.CANDIDATE_GENDER,
						IS_CANDIDATES_MARRIED = data_2.IS_CANDIDATES_MARRIED,HUSBAND_WIFE_NAME = data_2.HUSBAND_WIFE_NAME,NUMBER_OF_SURVIVING_CHILDREN 
						= data_2.NUMBER_OF_SURVIVING_CHILDREN,LAST_CHILD_DATE_OF_BIRTH = data_2.LAST_CHILD_DATE_OF_BIRTH,IS_THE_LAST_CHILD_TWIN = data_2.IS_THE_LAST_CHILD_TWIN,
						CANDIDATE_IS_A_WIDOW_DIVORCED_ABANDONED_WOMAN = data_2.CANDIDATE_IS_A_WIDOW_DIVORCED_ABANDONED_WOMAN,

						NATIVE_OF_MADHYA_PRADESH = data_2.NATIVE_OF_MADHYA_PRADESH,CATEGORY = data_2.CATEGORY,BELONGS_TO_CREAMY_LAYER = data_2.BELONGS_TO_CREAMY_LAYER,
						DISABILITY_CERTIFICATE = data_2.DISABILITY_CERTIFICATE,MINIMUM_40_PERCENT_DISABILITY = data_2.MINIMUM_40_PERCENT_DISABILITY,TYPE_OF_DISABILITY = data_2.TYPE_OF_DISABILITY,
						PERCENTAGE_OF_DISABILITY = data_2.PERCENTAGE_OF_DISABILITY,CANDIDATE_PUNISHED = data_2.CANDIDATE_PUNISHED,DEBARRED_PERIOD_FROM_ANY_EXAMINATION = data_2.DEBARRED_PERIOD_FROM_ANY_EXAMINATION,
						SERVING_IN_THE_GOVERNMENT = data_2.SERVING_IN_THE_GOVERNMENT,LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE = data_2.LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE,
						EX_SERVICEMAN = data_2.EX_SERVICEMAN,PERIOD_OF_SERVICE = data_2.PERIOD_OF_SERVICE,


						HSC_SUBJECT = data_3.HSC_SUBJECT,HSC_PERCENTAGE = data_3.HSC_PERCENTAGE,HSC_PASSING_YEAR = data_3.HSC_PASSING_YEAR,HSSC_SUBJECT = data_3.HSSC_SUBJECT,
						HSSC_PERCENTAGE = data_3.HSSC_PERCENTAGE,HSSC_PASSING_YEAR = data_3.HSSC_PASSING_YEAR,GRADUATION_SUBJECT = data_3.GRADUATION_SUBJECT,
						GRADUATION_PERCENTAGE = data_3.GRADUATION_PERCENTAGE,GRADUATION_PASSING_YEAR = data_3.GRADUATION_PASSING_YEAR,POST_GRADUATION_SUBJECT = data_3.POST_GRADUATION_SUBJECT,
						POST_GRADUATION_PERCENTAGE = data_3.POST_GRADUATION_PERCENTAGE,POST_PASSING_YEAR = data_3.POST_PASSING_YEAR,

						PRESENT_STATE = data_4.PRESENT_STATE,PRESENT_DISTRICT = data_4.PRESENT_DISTRICT,PRESENT_PIN_CODE = data_4.PRESENT_PIN_CODE,PRESENT_LAND_MARK = data_4.PRESENT_LAND_MARK,
						MOBILE_NUMBER = data_4.MOBILE_NUMBER,EMAIL_ID = data_4.EMAIL_ID,PRESENT_ADDRESS = data_4.PRESENT_ADDRESS,PERMANENT_STATE = data_4.PERMANENT_STATE,
						PERMANENT_DISTRICT = data_4.PERMANENT_DISTRICT,PERMANENT_PIN_CODE = data_4.PERMANENT_PIN_CODE,PERMANENT_LAND_MARK = data_4.PERMANENT_LAND_MARK,
						PERMANENT_ADDRESS = data_4.PERMANENT_ADDRESS,

						BANK_NAME = data_5.BANK_NAME,IFSC_CODE = data_5.IFSC_CODE,BRANCH_NAME = data_5.BRANCH_NAME,BRANCH_CODE = data_5.BRANCH_CODE,ACCOUNT_HOLDER_NAME = data_5.ACCOUNT_HOLDER_NAME,
						ACCOUNT_NUMBER = data_5.ACCOUNT_NUMBER,

						HIGH_SCHOOL = data_6.HIGH_SCHOOL,HSSC = data_6.HSSC,GRADUATION_MARKSHEET = data_6.GRADUATION_MARKSHEET,POST_GRADUATION = data_6.POST_GRADUATION,
						AADHAAR_CARD = data_6.AADHAAR_CARD,INCOME_CERTIFICATE=data_6.INCOME_CERTIFICATE,DISABLITY_CERTIFICATE=data_6.DISABLITY_CERTIFICATE,CAST_CERTIFICATE = data_6.CAST_CERTIFICATE,GATE_SCORECARD = data_6.GATE_SCORECARD,DEPARTMENTAL_NOC = data_6.DEPARTMENTAL_NOC,

						CHOICE_1 = data_7.CHOICE_1,CHOICE_2 = data_7.CHOICE_2,CHOICE_3 = data_7.CHOICE_3,CHOICE_4 = data_7.CHOICE_4,CHOICE_5 = data_7.CHOICE_5



				)
			submit_data.save()
			if  FlagDetail.objects.select_related('user').filter(user=request.user).exists():
				Flag_data = FlagDetail.objects.get(user=request.user)
				Flag_data.final_submit_flag=1
				Flag_data.save()
			else:
				Flag_data = FlagDetail(final_submit_flag=1,user=request.user)
				Flag_data.save()
			return redirect('/pdf/')

		else:
			return render(request,'Final_Submit.html',{'personal_value':data,'other_value':other_value})



	

@login_required(login_url='/singin')
def Pdfdata(request):
	Final_Data = FinalDataTable.objects.get(USER_CODE=request.user)

	return render(request,'pdf.html',{'Final_Data':Final_Data})

@login_required(login_url='/singin')
def UnpaidApplication(request):
	Add_Vacancy_Position = AddVacancyPosition.objects.all()
	Flag_data = FlagDetail.objects.select_related('user').filter(user=request.user) 

	
	return render(request,'Payment/UnpaidApplication.html',{'Add_Vacancy_Position':Add_Vacancy_Position,'Flag_data':Flag_data})

# this functions is useing for payment method
import payu_sdk
from paywix.payu import Payu
import uuid
txnid = uuid.uuid1()
import payu_sdk
from paywix.payu import Payu
from django.db.models import Q
import requests
import json
@login_required(login_url='/singin')	
def Candidate_Payment(request):
	if request.user.is_authenticated:
		Final_Data = FinalDataTable.objects.get(USER_CODE=request.user)
		# 7rnFly
		key = "M98tYu"
		# client = payu_sdk.payUClient(credes={"key": "GHeH7D", "salt": "DB2Y4tlzdBqPjFBiES3r5pf4c6JPQCtJ"}) #this for productions
		client = payu_sdk.payUClient(credes={"key": "M98tYu", "salt": "HkH31l4BahYcQ1kiwvIIFAinBRm5lfO7"}) # this is for uat
		if Final_Data.CATEGORY == 'UR':
			amount = 1000.0
			product = "student"
			name = Final_Data.FIRST_NAME
			last_name = Final_Data.LAST_NAME
			email = Final_Data.EMAIL_ID
			number = Final_Data.MOBILE_NUMBER
			param = {"txnid":txnid, "amount":amount, "productinfo":product,
					 "firstname":name,"email":email}
			apiHash = payu_sdk.Hasher.generate_hash(param)

			payment_data = PaymentDetail(
				user=request.user,net_amount_debit=amount,txnid=txnid,firstname=name,
				lastname=last_name,email=email,phone=number
				)
			payment_data.save()
			return render(request,'Payment/Candidate_Payment.html',{"posted": apiHash,"txnid":txnid,
				'amount':amount,"product":product,"name":name,"last_name":last_name,"email":email,'key':key,'number':number})
		else:
			amount = 600.0
			product = "student"
			name = Final_Data.FIRST_NAME
			last_name = Final_Data.LAST_NAME
			email = Final_Data.EMAIL_ID
			number = Final_Data.MOBILE_NUMBER
			param = {"txnid":txnid, "amount":amount, "productinfo":product,
					 "firstname":name,"email":email}
			apiHash = payu_sdk.Hasher.generate_hash(param)

			payment_data = PaymentDetail(
				user=request.user,net_amount_debit=amount,txnid=txnid,firstname=name,
				lastname=last_name,email=email,phone=number
				)
			payment_data.save()
			return render(request,'Payment/Candidate_Payment.html',{"posted": apiHash,"txnid":txnid,
				'amount':amount,"product":product,"name":name,"last_name":last_name,"email":email,'key':key,'number':number})

	else:
		return redirect('/login/')

@csrf_exempt
def payu_success_registration(request):
    data = {k: v[0] for k, v in dict(request.POST).items()}
    print(data)
    Hash = data['hash']
    Status = data['status']
    Txn_id = data['txnid']
    Product_info = data['productinfo']
    First_name = data['firstname']
    Last_name = data['lastname']
    Phone_no = data['phone']
    mail = data['email']
    Pgateway_Type = data['PG_TYPE']
    Bankrefnum = data['bank_ref_num']
    Bank_code = data['bankcode']
    payu_moneyid = data['mihpayid']
    Netamount = data['net_amount_debit']
    addedon = data['addedon']
    mode = data['mode']
    # request.session['Phone_no'] = Phone_no
    if Pgateway_Type == 'NB-PG':
        if PaymentDetail.objects.filter(txnid=Txn_id).exists():
            Payudata = PaymentDetail.objects.get(Txdid=Txn_id)
            Payudata.mihpayid = payu_moneyid
            Payudata.hash_key = Hash
            Payudata.PG_TYPE = Pgateway_Type
            # Payudata.date = date
            Payudata.bank_ref_num = Bankrefnum
            Payudata.addedon = addedon
            Payudata.bankcode = Bank_code
            payudata.mode = mode
            Payudata.Name_On_Card =  'Not Available'
            Payudata.cardnum =  'Not Available'

            Payudata.status=Status
            Payudata.save()
    elif mode =='NB':
    	if PaymentDetail.objects.filter(txnid=Txn_id).exists():
            Payudata = PaymentDetail.objects.get(txnid=Txn_id)
            Payudata.mihpayid = payu_moneyid
            Payudata.hash_key = Hash
            Payudata.PG_TYPE = Pgateway_Type
            # Payudata.date = date
            Payudata.bank_ref_num = Bankrefnum
            Payudata.bankcode = Bank_code
            Payudata.addedon = addedon
            Payudata.mode = mode
           
            Payudata.status=Status
            Payudata.save()
    elif mode =='CC':
    	if PaymentDetail.objects.filter(txnid=Txn_id).exists():
            Card_num = data['cardnum']
            Payudata = PaymentDetail.objects.get(txnid=Txn_id)
            Payudata.mihpayid = payu_moneyid
            Payudata.hash_key = Hash
            Payudata.PG_TYPE = Pgateway_Type
            Payudata.bank_ref_num = Bankrefnum
            Payudata.bankcode = Bank_code
            Payudata.addedon = addedon
            Payudata.mode = mode
            Payudata.cardnum = Card_num
            Payudata.status=Status
            Payudata.save()

    elif mode =='UPI':
    	if PaymentDetail.objects.filter(txnid=Txn_id).exists():
            Payudata = PaymentDetail.objects.get(txnid=Txn_id)
            Payudata.mihpayid = payu_moneyid
            Payudata.hash_key = Hash
            Payudata.PG_TYPE = Pgateway_Type
            Payudata.bank_ref_num = Bankrefnum
            Payudata.bankcode = Bank_code
            Payudata.addedon = addedon
            Payudata.mode = mode
            Payudata.status=Status
            Payudata.save()





    else:
        if PaymentDetail.objects.filter(txnid=Txn_id).exists():
            Card_num = data['cardnum']
            Payudata = PaymentDetail.objects.get(txnid=Txn_id)
            Payudata.mihpayid = payu_moneyid
            Payudata.hash_key = Hash
            Payudata.PG_TYPE = Pgateway_Type
            Payudata.bank_ref_num = Bankrefnum
            Payudata.bankcode = Bank_code
            Payudata.addedon = addedon
            Payudata.mode = mode
            Payudata.cardnum = Card_num
            Payudata.status=Status
            Payudata.save()
    # user = User_Registration_CA.objects.get(Mobile=Phone_no)
    # user.Payment_Status=1
    # user.Is_Enable=1
    # user.save()
    
    # model = User_Registration_CA.objects.filter(Mobile=Phone_no)
    # model.update(Payment_Status=1)
    # # model.update(RegistractionNumber=s)
    # Regdatashow = User_Registration_CA.objects.filter(Mobile=Phone_no)
    # # date = datetime.now()
    # user = User_Registration_CA.objects.get(Mobile=Phone_no)
    client = payu_sdk.payUClient(credes={"key": "M98tYu", "salt": "HkH31l4BahYcQ1kiwvIIFAinBRm5lfO7"}) #this is for testing
    # client = payu_sdk.payUClient(credes={"key":"GHeH7D","salt":"DB2Y4tlzdBqPjFBiES3r5pf4c6JPQCtJ"}) # this is for producions
    
    key = 'M98tYu'
    salt = 'HkH31l4BahYcQ1kiwvIIFAinBRm5lfO7'
    command = 'verify_payment'
    toHash = {"command": command, "var1": Txn_id}
    apiHash = payu_sdk.Hasher.APIHash(toHash)
    Poststring = "key=" + key + "&command=" + command + "&hash=" + apiHash + "&var1=" + Txn_id;
    url = 'https://test.payu.in/merchant/postservice.php?form=2' #This is for testing
    proxyDictfd={"https":"proxy.mpcz.in:8080","http":"proxy.mpcz.in:8080"} # comment when working with uat 
    # response = requests.get(url,proxies=proxyDictfd)
    # r = requests.post(url, data=Poststring)
    # url = "https://info.payu.in/merchant/postservice?form=2"
    headers = {"Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
    payload = "key=" + key + "&command=verify_payment&var1=" + Txn_id + "&hash=" + apiHash
    res = requests.request("POST", url,proxies=proxyDictfd, data=payload, headers=headers) # this is for uat server
    # res = requests.request("POST",url,data=payload, headers=headers)# un comment this when code in production 
    print(res)

    if res.status_code == 200:
        json_data = json.loads(res.text)
        if json_data['status'] == 1:
            transcation_details = json_data['transaction_details']
            transction_data = transcation_details[Txn_id]
            if transction_data['status'] == 'success':
                payu_obj = PaymentDetail.objects.get(txnid=Txn_id)
                if transction_data['productinfo'] == "student":
                    user = FinalDataTable.objects.get(USER_CODE=payu_obj.user)#for paymnet flag in final table of candidate 
                    
                    user.payment = True
                    user.save()
                    Flag_table = FlagDetail.objects.get(user=payu_obj.user)
                    Flag_table.payment_flag = True
                    Flag_table.save()
                    def Generate_ApNo():
                    	RegNum = "AECR2022"
                    	list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                    	Gen_Ap_No = ""
                    	Gen_Ap_No = Gen_Ap_No + "V" + RegNum + random.choice(list1) + random.choice(list1) + random.choice(list1) + random.choice(list1)
                    	if FinalDataTable.objects.filter(Application_Number=Gen_Ap_No).exists():
                    		return Generate_ApNo()
                    	else:
                    		user.Application_Number = Gen_Ap_No
                    		user.save()




                    return render(request, 'Payment/Payment_Success.html',{'data':payu_obj,'user':user})
                return render(request, 'Payment/Payment_Success.html', {'data': payu_obj})
    else:
        attempt_num += 1
        time.sleep(5)  # Wait for 5 seconds before re-trying

    # request.session['Phone_no'] = Phone_no
    # print('this is session',request.session['Phone_no'])
    return render(request, 'Payment/Payment_Success.html', {'data': payu_obj})

def payu_fail(request):
	return render(request,'Payment/Payment_Fail.html')
   


 






############## ##################################################################################################################################
@login_required(login_url='/singin')
def Application_Number(request):
	Flag_data = FlagDetail.objects.select_related('user').filter(user=request.user)
	if FinalDataTable.objects.select_related('USER_CODE').filter(USER_CODE=request.user).exists():
		Ap_No = FinalDataTable.objects.get(USER_CODE=request.user)
		return render(request,'ApplicationNumber/ApplicationNumber.html',{'Flag_data':Flag_data,'Ap_No':Ap_No})
	else:
		return render(request,'ApplicationNumber/ApplicationNumber.html',{'Flag_data':Flag_data})
@login_required(login_url='/singin')	
def Candidate_declaration(request):
	return render(request,'Candidate_declaration.html')

# show blog data and blog details 
@login_required(login_url='/singin')	
def blog_details(request,id):
	
	return render(request,'blog_details.html')
@login_required(login_url='/singin')	
def Apply(request):
	Current_Date = date.today()
	Vacancy = AddVacancyPosition.objects.all()
	Total_Vacancy = AddVacancyPosition.objects.all().count()
	return render(request,'apply.html',{'Vacancy':Vacancy,'Total_Vacancy':Total_Vacancy,'Current_Date':Current_Date})



### User profile
#@login_required(login_url='/singin')
def my_profile(request):
	Vacancy = AddVacancyPosition.objects.all()
	
	return render(request,'Myprofile.html',{'Vacancy':Vacancy})

## User project
# @login_required(login_url='/singin')	
def my_project(request):
	
	return render(request,'Myprojects.html')

# gernal information 
@login_required(login_url='/singin')	
def genralinformation(request):
	
	return render(request,'genral_information.html')
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


### this for change password
@login_required(login_url='/singin')
def passChange(request):
	if request.method=='POST':
		form=Password_change(request.user,request.POST or None)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request,user)
			messages.success(request,'Your password was successfully updated!')

			return redirect('/passChange')
		else:
			messages.error(request,'Please correct the error below')
			form=Password_change(request.user,request.POST or None)
			return render(request,'Change_password.html',{'curl':curl,'form':form})
	else:
		form=Password_change(request.user,request.POST or None)
		footerdata=footer_data.objects.all()
		return render(request,'Change_password.html',{'curl':curl,'form':form,'footerdata':footerdata})




