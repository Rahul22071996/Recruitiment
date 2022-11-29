from django import forms
from django.views.generic.edit import FormMixin
from .models import *
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User


# class Personal_Details_form(forms.ModelForm):
# 	DEPARTMENTAL = (('YES','YES'),('NO','NO'))
# 	Is_Applicant_A_Departmental_Candidate = forms.ChoiceField(choices=DEPARTMENTAL, widget=forms.RadioSelect)
# 	class Meta:
# 		model = PersonalDetails
# 		fields = {"Is_Applicant_A_Departmental_Candidate"}





class user_enquiry_form(forms.ModelForm):
	username=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control underline'}),label='username')
	email=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control underline'}),label='email')
	subject=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control underline'}),label='subject')
	description=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control underline'}),label='description')
	token=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control underline'}),label='token')

	class Meta:
		model=user_enquiry
		fields={"username","email","subject","description","token"}

class Password_change(FormMixin,PasswordChangeForm):
	def __init__(self,*args,**Kwargs):
		super().__init__(*args,**Kwargs)
		self.fields['old_password'].widget.attrs.update({'class' :'form-control','placeholder':'Old Password'})
		self.fields['new_password1'].widget.attrs.update({'class' :'form-control','placeholder':'New Password'})
		self.fields['new_password2'].widget.attrs.update({'class' :'form-control','placeholder':'Confirm New Password'})
class CreateUserform(UserCreationForm):
	first_name=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control','placeholder':'first name'}),label='First Name')
	last_name=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control','placeholder':'last name'}),label='First Name')
	email=forms.CharField(widget=forms.EmailInput( attrs={'class' :'form-control','placeholder':'email'}),label='First Name')
	password1=forms.CharField(widget=forms.PasswordInput( attrs={'class' :'form-control','placeholder':'Enter your password','id':"password-field"}),label='First Name')
	password2=forms.CharField(widget=forms.PasswordInput( attrs={'class' :'form-control','placeholder':'Re-enter password','id':"repass-field"}),label='First Name')
	username=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control','placeholder':'user name'}),label='First Name',min_length=5,max_length=150)
	class Meta:
		model=User
		fields={'email','password1','password2','username','first_name','last_name'}

class userprofileform(forms.ModelForm):
	phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone number','id':'mobilenumber','required':'True'}),label='Phone number',min_length=10,max_length=10)
	
	
	class Meta:
		model=userprofile
		fields={'phone'}

class Userupdateform(forms.ModelForm):
	first_name=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control','placeholder':'first name'}),label='First Name')
	last_name=forms.CharField(widget=forms.TextInput( attrs={'class' :'form-control','placeholder':'last name'}),label='First Name')
	email=forms.CharField(widget=forms.EmailInput( attrs={'class' :'form-control','placeholder':'email','readonly':'readonly'}),label='First Name')
	class Meta:
		model=User
		fields={'email','first_name','last_name'}

class Userprofileupdateform(forms.ModelForm):
	phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Phone number'}),label='Phone number')
	class Meta:
		model=userprofile
		fields={'phone'}


# class PaymentPaytm_form(forms.ModelForm):
	# username=forms.CharField(widget=forms.TextInput( attrs={'class':"form-control",'placeholder':'username'}),label='username')
	# email=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Email Id'}),label='email')
	# paytmNumber=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Paytm Number'}),label='subject')
	# ProjectName=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Project Name'}),label='description')
	# 

	# class Meta:
		# model=PaymentPaytm
		# fields={"username","email","paytmNumber","ProjectName"}



# class PaymentGooglepay_form(forms.ModelForm):
	# username=forms.CharField(widget=forms.TextInput( attrs={'class':"form-control",'placeholder':'username'}),label='username')
	# email=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Email Id'}),label='email')
	# Googlepay=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Googlepay Number'}),label='subject')
	# ProjectName=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Project Name'}),label='description')
	# 

	# class Meta:
		# model=PaymentGooglepay
		# fields={"username","email","Googlepay","ProjectName"}



# class PaymentBank_form(forms.ModelForm):
# 	username=forms.CharField(widget=forms.TextInput( attrs={'class':"form-control",'placeholder':'username'}),label='username')
# 	email=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Email Id'}),label='email')
# 	AccountNumber=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Account Number'}),label='subject')
# 	ProjectName=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Project Name'}),label='description')
# 	IfscCode=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'IFSC code'}),label='email')
# 	BankName=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Bank Name'}),label='subject')
# 	Branch=forms.CharField(widget=forms.TextInput(  attrs={'class':"form-control",'placeholder':'Branch'}),label='description')
	

# 	class Meta:
# 		model=PaymentBank
# 		fields={"username","email","BankName","ProjectName","Branch","AccountNumber","IfscCode",}
