from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator
from django.conf import settings
from django.contrib.auth import get_user_model
User=get_user_model()
# applicant user registracion models start
# GENDER = (('MALE','MALE'),('FEMALE','FEMALE'))
# 	Gender = models.CharField(max_length=255,choices=GENDER, null=True)

 
#this is for choice fillig
NATIVE_COUNTRY =(('INDIAN','INDIAN'),('OTHER','OTHER'))

TYPE_OF_EMPLOYMENT = (('Regular','Regular'),('Contractual','Contractual'))
CHOICEFILLING = (	('MPPKVVCL BHOPAL','MPPKVVCL BHOPAL'),
					('MPPKVVCL JABALPUR','MPPKVVCL JABALPUR'),('MPPKVVCL INDORE','MPPKVVCL INDORE'),
					('MPTRANSCO','MPTRANSCO'),('MPGENCO','MPGENCO'),('MPPMCL','MPPMCL')
					)

POSTAPPLIED = (
	('Asstistant Engineer/Manager - Technical/Distribution/Transmission/Genration(Electrical)','Asstistant Engineer/Manager - Technical/Distribution/Transmission/Genration(Electrical)'),('Asstistant Engineer/Manager - Genration(Mechanical)','Asstistant Engineer/Manager - Genration(Mechanical)'),
	('Asstistant Engineer/Manager (Civil)','Asstistant Engineer/Manager (Civil)'),('Asstistant Engineer/Manager (IT)','Asstistant Engineer/Manager (IT)')

	)
# this is for personal Details 
CHOICES = (('YES','YES'),('NO','NO'))
GENDER = (('MALE','MALE'),('FEMALE','FEMALE'))
CATEGORYDATA = (('UR','UR'),('SC','SC'),('ST','ST'),('OBC','OBC'),('EWS','EWS'))
TYPE_OF_DISABILITY_OPSTION = (('Fractured(OH)','Fractured(OH)'),('Vision Impaired(VH)','Vision Impaired(VH)'),
		('Hearing Impairment(HH)','Hearing Impairment(HH)'),('Multiple Disabilities(MD)','Multiple Disabilities(MD)'))
class PersonalDetail(models.Model):
	USER_CODE = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	IS_APPLICANT_A_DEPARTMENTAL_CANDIDATE = models.CharField(max_length=3,choices=CHOICES,null=True,blank=True)
	EMPLOYMENT_TYPE = models.CharField(max_length=255,choices=TYPE_OF_EMPLOYMENT,null=True,blank=True)
	POSTED_SINCE = models.DateField(blank=True,null=True)
	GATE_SCORE_YEAR = models.CharField(max_length=6,blank=True,null=True)
	GATE_SCORE = models.PositiveIntegerField(null=True,blank=True)
	GATE_ROLL_NO = models.CharField(max_length=255,blank=True,null=True)
	POST_APPLIED_FOR = models.CharField(max_length=255,choices=POSTAPPLIED,null=True,blank=True)
	AADHAAR_CARD_NO = models.CharField(max_length=12)
	FIRST_NAME = models.CharField(max_length=50)
	MIDDLE_NAME = models.CharField(max_length=50,null=True,blank=True)
	LAST_NAME = models.CharField(max_length=50)
	FATHER_NAME = models.CharField(max_length=50)
	MOTHER_NAME = models.CharField(max_length=50)
	DATE_OF_BIRTH = models.DateField(blank=True,null=True)
	CANDIDATE_GENDER = models.CharField(max_length=55,choices=GENDER,null=True,blank=True)
	
# this is for other details  

class OtherDetail(models.Model):
	USER_CODE = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	IS_CANDIDATES_MARRIED = models.CharField(max_length=5,choices=CHOICES,null=True,blank=True)
	HUSBAND_WIFE_NAME  = models.CharField(max_length=50,null=True,blank=True)
	NUMBER_OF_SURVIVING_CHILDREN = models.PositiveIntegerField(blank=True,null=True)
	LAST_CHILD_DATE_OF_BIRTH = models.DateField(blank=True,null=True)
	IS_THE_LAST_CHILD_TWIN = models.CharField(max_length=5,choices=CHOICES,null=True,blank=True)
	CANDIDATE_IS_A_WIDOW_DIVORCED_ABANDONED_WOMAN = models.CharField(max_length=5,choices=CHOICES,null=True,blank=True)

	COUNTRY = models.CharField(max_length=8,choices=NATIVE_COUNTRY,null=True,blank=True)
	NATIVE_OF_MADHYA_PRADESH = models.CharField(max_length=3,choices=CHOICES,null=True)
	CATEGORY = models.CharField(max_length=3,choices=CATEGORYDATA,null=True)
	BELONGS_TO_CREAMY_LAYER = models.CharField(max_length=255,choices=CHOICES,null=True)
	DISABILITY_CERTIFICATE = models.CharField(max_length=255,choices=CHOICES,null=True)
	MINIMUM_40_PERCENT_DISABILITY = models.CharField(max_length=255,choices=CHOICES,null=True)
	TYPE_OF_DISABILITY =  models.CharField(max_length=255,choices=TYPE_OF_DISABILITY_OPSTION,null=True)
	PERCENTAGE_OF_DISABILITY = models.CharField(max_length=5,null=True,blank=True,default=" ")
	CANDIDATE_PUNISHED =  models.CharField(max_length=5,choices=CHOICES,null=True)
	DEBARRED_PERIOD_FROM_ANY_EXAMINATION = models.CharField(max_length=255,choices=CHOICES,null=True)
	SERVING_IN_THE_GOVERNMENT = models.CharField(max_length=255,choices=CHOICES,null=True)
	LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE = models.CharField(max_length=255,choices=CHOICES,null=True)
	INTER_CASTE_MARRIAGE = models.CharField(max_length=3,choices=CHOICES,null=True)
	VIKRAM_AWARDEE_SPORTSPERSON = models.CharField(max_length=3,choices=CHOICES,null=True)
	EX_SERVICEMAN = models.CharField(max_length=3,choices=CHOICES,null=True)
	PERIOD_OF_SERVICE = models.PositiveIntegerField(null=True,blank=True)


# this is for eduction details
class EducationDetails(models.Model):
	USER_CODE = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	#10th
	HSC_SUBJECT = models.CharField(max_length=15,null=True,blank=True)
	HSC_PERCENTAGE = models.CharField(max_length=15,null=True,blank=True)
	HSC_PASSING_YEAR = models.CharField(max_length=15,null=True,blank=True)
	#12 th
	HSSC_SUBJECT = models.CharField(max_length=15,null=True,blank=True)
	HSSC_PERCENTAGE = models.CharField(max_length=15,null=True,blank=True)
	HSSC_PASSING_YEAR = models.CharField(max_length=15,null=True,blank=True)
	# graduation
	GRADUATION_SUBJECT = models.CharField(max_length=15,null=True,blank=True)
	GRADUATION_PERCENTAGE = models.CharField(max_length=15,null=True,blank=True)
	GRADUATION_PASSING_YEAR = models.CharField(max_length=15,null=True,blank=True)
	#post graduation
	POST_GRADUATION_SUBJECT = models.CharField(max_length=15,null=True,blank=True)
	POST_GRADUATION_PERCENTAGE = models.CharField(max_length=15,null=True,blank=True)
	POST_PASSING_YEAR = models.CharField(max_length=15,null=True,blank=True)
	

# Address details
# from django.core.exceptions import ValidationError
 
# # creating a validator function
# def validate_EMAIL_ID(value):
#     if "@gmail.com" in value:
#         return value
#     else:
#         raise ValidationError("This field accepts mail id of google only")

class AddressDetail(models.Model):
	USER_CODE = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	PRESENT_STATE = models.CharField(max_length=255,null=True,blank=True)
	PRESENT_DISTRICT = models.CharField(max_length=255,null=True,blank=True)
	PRESENT_PIN_CODE = models.CharField(max_length=255,null=True,blank=True)
	PRESENT_LAND_MARK = models.CharField(max_length=255,null=True,blank=True)
	MOBILE_NUMBER = models.CharField(max_length=255,null=True,blank=True)
	EMAIL_ID = models.EmailField(max_length=255,null=True,blank=True)
	PRESENT_ADDRESS = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_STATE = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_DISTRICT = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_PIN_CODE = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_LAND_MARK = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_ADDRESS = models.CharField(max_length=255,null=True,blank=True)

# Bank Details

class BankDetail(models.Model):
	USER_CODE = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	BANK_NAME = models.CharField(max_length=255,null=True,blank=True)
	IFSC_CODE = models.CharField(max_length=255,null=True,blank=True)
	BRANCH_NAME = models.CharField(max_length=255,null=True,blank=True)
	BRANCH_CODE = models.CharField(max_length=255,null=True,blank=True)
	ACCOUNT_HOLDER_NAME = models.CharField(max_length=255,null=True,blank=True)
	ACCOUNT_NUMBER = models.CharField(max_length=255,null=True,blank=True)


# Upload document 

class DocumentUpload(models.Model):
	USER_CODE = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	HIGH_SCHOOL = models.FileField(upload_to ='PDF/HIGH_SCHOOL')
	HSSC = models.FileField(upload_to ='PDF/HSSC')
	GRADUATION_MARKSHEET = models.FileField(upload_to ='PDF/GRADUATION_MARKSHEET')
	POST_GRADUATION = models.FileField(upload_to ='PDF/HIGH_SCHOOL')
	AADHAAR_CARD = models.FileField(upload_to ='PDF/POST_GRADUATION')
	CAST_CERTIFICATE = models.FileField(upload_to ='PDF/CAST_CERTIFICATE')
	GATE_SCORECARD = models.FileField(upload_to ='PDF/GATE_SCORECARD')
	DEPARTMENTAL_NOC = models.FileField(upload_to ='PDF/DEPARTMENTAL_NOC',blank=True,null=True)
	INCOME_CERTIFICATE = models.FileField(upload_to='PDF/INCOME_CERTIFICATE',blank=True,null=True)
	DISABLITY_CERTIFICATE = models.FileField(upload_to='PDF/DISABLITY_CERTIFICATE',blank=True,null=True)

# CHOICE FILLING

class ChoiceFilling(models.Model):
	USER_CODE = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	CHOICE_1 = models.CharField(max_length=255,choices=CHOICEFILLING)

	CHOICE_2 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)
	CHOICE_3 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)
	CHOICE_4 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)
	CHOICE_5 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)
	CHOICE_6 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)



# this is all data_save tabel to save
class FinalDataTable(models.Model):
	USER_CODE = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	Application_Number = models.CharField(max_length=255,null=True,blank=True,unique=True)
	IS_APPLICANT_A_DEPARTMENTAL_CANDIDATE = models.CharField(max_length=3,choices=CHOICES,null=True,blank=True)
	IS_APPLICANT_GATE_QUALIFIED = models.CharField(max_length=255,choices=CHOICES,null=True,blank=True)
	EMPLOYMENT_TYPE = models.CharField(max_length=255,choices=TYPE_OF_EMPLOYMENT,null=True,blank=True)
	POSTED_SINCE = models.DateField(blank=True,null=True)

	GATE_SCORE_YEAR = models.CharField(max_length=6,blank=True,null=True)
	GATE_SCORE = models.PositiveIntegerField(null=True,blank=True)
	GATE_ROLL_NO = models.CharField(max_length=255,blank=True,null=True)
	AADHAAR_CARD_NO = models.CharField(max_length=12)
	FIRST_NAME = models.CharField(max_length=50)
	MIDDLE_NAME = models.CharField(max_length=50,null=True,blank=True)
	LAST_NAME = models.CharField(max_length=50)
	FATHER_NAME = models.CharField(max_length=50)
	MOTHER_NAME = models.CharField(max_length=50)
	DATE_OF_BIRTH = models.DateField(null=True,blank=True)
	CANDIDATE_GENDER = models.CharField(max_length=55,choices=GENDER,null=True,blank=True)
	IS_CANDIDATES_MARRIED = models.CharField(max_length=5,choices=CHOICES,null=True,blank=True)
	HUSBAND_WIFE_NAME  = models.CharField(max_length=50,null=True,blank=True)
	NUMBER_OF_SURVIVING_CHILDREN = models.PositiveIntegerField(blank=True,null=True)
	LAST_CHILD_DATE_OF_BIRTH = models.DateField(blank=True,null=True)
	IS_THE_LAST_CHILD_TWIN = models.CharField(max_length=5,choices=CHOICES,null=True,blank=True)
	CANDIDATE_IS_A_WIDOW_DIVORCED_ABANDONED_WOMAN = models.CharField(max_length=5,choices=CHOICES,null=True,blank=True)
	# this is for other details
	NATIVE_OF_MADHYA_PRADESH = models.CharField(max_length=3,choices=CHOICES,null=True)
	CATEGORY = models.CharField(max_length=3,choices=CATEGORYDATA,null=True)
	BELONGS_TO_CREAMY_LAYER = models.CharField(max_length=255,choices=CHOICES,null=True)
	DISABILITY_CERTIFICATE = models.CharField(max_length=255,choices=CHOICES,null=True)
	MINIMUM_40_PERCENT_DISABILITY = models.CharField(max_length=255,choices=CHOICES,null=True)
	TYPE_OF_DISABILITY =  models.CharField(max_length=255,choices=TYPE_OF_DISABILITY_OPSTION,null=True)
	PERCENTAGE_OF_DISABILITY = models.CharField(max_length=5,null=True,blank=True,default=" ")
	CANDIDATE_PUNISHED =  models.CharField(max_length=5,choices=CHOICES,null=True)
	DEBARRED_PERIOD_FROM_ANY_EXAMINATION = models.CharField(max_length=255,choices=CHOICES,null=True)
	SERVING_IN_THE_GOVERNMENT = models.CharField(max_length=255,choices=CHOICES,null=True)
	LIVE_REGISTRATION_IN_THE_EMPLOYMENT_OFFICE = models.CharField(max_length=255,choices=CHOICES,null=True)
	EX_SERVICEMAN = models.CharField(max_length=3,choices=CHOICES,null=True)
	PERIOD_OF_SERVICE = models.PositiveIntegerField(null=True,blank=True)
	# this is for eduction details
	#10th
	HSC_SUBJECT = models.CharField(max_length=15,null=True,blank=True)
	HSC_PERCENTAGE = models.CharField(max_length=15,null=True,blank=True)
	HSC_PASSING_YEAR = models.CharField(max_length=15,null=True,blank=True)
	#12 th
	HSSC_SUBJECT = models.CharField(max_length=15,null=True,blank=True)
	HSSC_PERCENTAGE = models.CharField(max_length=15,null=True,blank=True)
	HSSC_PASSING_YEAR = models.CharField(max_length=15,null=True,blank=True)
	# graduation
	GRADUATION_SUBJECT = models.CharField(max_length=15,null=True,blank=True)
	GRADUATION_PERCENTAGE = models.CharField(max_length=15,null=True,blank=True)
	GRADUATION_PASSING_YEAR = models.CharField(max_length=15,null=True,blank=True)
	#post graduation
	POST_GRADUATION_SUBJECT = models.CharField(max_length=15,null=True,blank=True)
	POST_GRADUATION_PERCENTAGE = models.CharField(max_length=15,null=True,blank=True)
	POST_PASSING_YEAR = models.CharField(max_length=15,null=True,blank=True)
	# this is for Address
	PRESENT_STATE = models.CharField(max_length=255,null=True,blank=True)
	PRESENT_DISTRICT = models.CharField(max_length=255,null=True,blank=True)
	PRESENT_PIN_CODE = models.CharField(max_length=255,null=True,blank=True)
	PRESENT_LAND_MARK = models.CharField(max_length=255,null=True,blank=True)
	MOBILE_NUMBER = models.CharField(max_length=255,null=True,blank=True)
	EMAIL_ID = models.EmailField(max_length=255,null=True,blank=True)
	PRESENT_ADDRESS = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_STATE = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_DISTRICT = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_PIN_CODE = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_LAND_MARK = models.CharField(max_length=255,null=True,blank=True)
	PERMANENT_ADDRESS = models.CharField(max_length=255,null=True,blank=True)
	# this is for Bank details
	BANK_NAME = models.CharField(max_length=255,null=True,blank=True)
	IFSC_CODE = models.CharField(max_length=255,null=True,blank=True)
	BRANCH_NAME = models.CharField(max_length=255,null=True,blank=True)
	BRANCH_CODE = models.CharField(max_length=255,null=True,blank=True)
	ACCOUNT_HOLDER_NAME = models.CharField(max_length=255,null=True,blank=True)
	ACCOUNT_NUMBER = models.CharField(max_length=255,null=True,blank=True)
	# this is for Document Upload
	HIGH_SCHOOL = models.FileField(upload_to ='FINALPDF/HIGH_SCHOOL')
	HSSC = models.FileField(upload_to ='FINALPDF/HSSC')
	GRADUATION_MARKSHEET = models.FileField(upload_to ='FINALPDF/GRADUATION_MARKSHEET')
	POST_GRADUATION = models.FileField(upload_to ='FINALPDF/HIGH_SCHOOL')
	AADHAAR_CARD = models.FileField(upload_to ='FINALPDF/POST_GRADUATION')
	CAST_CERTIFICATE = models.FileField(upload_to ='FINALPDF/CAST_CERTIFICATE')
	GATE_SCORECARD = models.FileField(upload_to ='FINALPDF/GATE_SCORECARD')
	DEPARTMENTAL_NOC = models.FileField(upload_to ='FINALPDF/DEPARTMENTAL_NOC',blank=True,null=True)
	INCOME_CERTIFICATE = models.FileField(upload_to='FINALPDF/INCOME_CERTIFICATE',blank=True,null=True)
	DISABLITY_CERTIFICATE = models.FileField(upload_to='FINALPDF/DISABLITY_CERTIFICATE',blank=True,null=True)
	# this is for Choice filling
	CHOICE_1 = models.CharField(max_length=255,choices=CHOICEFILLING)
	CHOICE_2 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)
	CHOICE_3 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)
	CHOICE_4 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)
	CHOICE_5 = models.CharField(max_length=255,choices=CHOICEFILLING,blank=True,null=True)
	# payment details
	payment = models.BooleanField(default=False)


#flag to check the data is submitted or not if flag is one  its meain data for the table is  already submitted 

class FlagDetail(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	personal_detail_flag = models.BooleanField(default=False)
	other_detail_flag = models.BooleanField(default=False)
	education_details_flag = models.BooleanField(default=False)
	address_detail_flag = models.BooleanField(default=False)
	bank_detail_flag = models.BooleanField(default=False)
	document_upload_flag = models.BooleanField(default=False)
	choice_filling_flag = models.BooleanField(default=False)
	payment_flag = models.BooleanField(default=False)
	final_submit_flag = models.BooleanField(default=False)








class PaymentDetail(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
	mihpayid = models.CharField(max_length=100,blank=True,null=True)
	net_amount_debit = models.CharField(max_length=100,default=0)
	txnid = models.CharField(max_length=500,blank=True,null=True)
	mode = models.CharField(max_length=100,blank=True,null=True)
	status = models.CharField(max_length=100,blank=True,null=True)
	addedon = models.DateTimeField(blank=True,null=True)
	firstname = models.CharField(max_length=100,blank=True,null=True)
	lastname = models.CharField(max_length=100,blank=True,null=True)
	email = models.EmailField(max_length=100,blank=True,null=True)
	phone = models.CharField(max_length=100,blank=True,null=True)
	hash_key = models.CharField(max_length=1000,blank=True,null=True)
	address1 = models.CharField(max_length=100,blank=True,null=True)
	city = models.CharField(max_length=100,blank=True,null=True)
	state = models.CharField(max_length=100,blank=True,null=True)
	PG_TYPE = models.CharField(max_length=100,blank=True,null=True)
	bank_ref_num = models.CharField(max_length=100,blank=True,null=True)
	cardnum = models.CharField(max_length=100,blank=True,null=True)
	bankcode = models.CharField(max_length=100,blank=True,null=True)

















































# user enquiry model 
class user_enquiry(models.Model):
	username=models.CharField(max_length=255)
	email=models.EmailField(max_length=255)
	subject=models.CharField(max_length=255)
	description=models.TextField()
	date=models.DateField(auto_now=True)
	token=models.CharField(max_length=255)
	status=models.IntegerField(default=1)


#user profile 
class userprofile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	phone=models.CharField(max_length=255)
	
def create_profile(sender,**kwargs):
	if kwargs['created']:
		user_profile=userprofile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile,sender=User)
# business enquire 	
class business_enquire(models.Model):
	company_name=models.CharField(max_length=255)
	company_email=models.EmailField(max_length=255)
	company_subject=models.CharField(max_length=255)
	company_description=models.TextField()
	company_contact=models.CharField(max_length=10)
	company_date=models.DateField(auto_now=True)
	company_token=models.CharField(max_length=255)
	company_status=models.IntegerField(default=1)
# this assign project 
class assignproject(models.Model):
	assignuser=models.CharField(max_length=255)
	assignproject=models.CharField(max_length=255)
	amount=models.CharField(max_length=255)
	ProjectName=models.CharField(max_length=255,default='')
	Companyname=models.CharField(max_length=255,default='')
	skills=models.CharField(max_length=255,default='')
	Description=models.TextField(default='')
	Date=models.DateField(auto_now=True)
	Duration=models.CharField(max_length=255,default='')
	location=models.CharField(max_length=255,default=True)
	status=models.IntegerField(default=0)
	createdate=models.DateField(auto_now=True,blank=True)
	Image=models.CharField(max_length=255,blank=True)
	


################################payment mode ##################################33
