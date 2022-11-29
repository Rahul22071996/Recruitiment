from django.urls import path
from django.conf.urls.static import  static
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[path('',views.home),
			
			
			# path('contact_us/',views.contact),
			path('singin/',views.Singin),
			path('singup/',views.Singup),
			path('personal/details/',views.personal_details),
			path('other/details/',views.other_details),
			path('education/details/',views.education_details),
			path('address/details/',views.address),
			path('bank/details/',views.bank_details),
			path('document/upload/',views.document_upload),
			path('choice/filling/',views.choice_filling),
			path('Apply/',views.Apply),
			path('logout/',views.handlelogout),
			
			
			path('blog_details/<int:id>',views.blog_details),
			#path('userdetails/',views.userdetails),
			path('Advertisement/',views.my_profile),
			path('UnpaidApplication/',views.UnpaidApplication,name="UnpaidApplication"),
			path('Application-Number/',views.Application_Number,name="Application_Number"),
			path('my_project/',views.my_project),
			path('genralinformation/',views.genralinformation),
			path('profileedit/',views.profileedit),
			path('pdf/',views.Pdfdata),
			path('Candidate_declaration/',views.Candidate_declaration),
			path('Final_Submit/',views.Final_Submit),
			path('Candidate/Payment/',views.Candidate_Payment),
			path('Flat/redirect/',views.flag_details),# this url is using for redirect the user according to their form filled.

			path('payment/success/',views.payu_success_registration,name="payu_success_registration"),
			path('payment/failure/',views.payu_fail,name="payu_fail"),


			# this sectaion for forget password
			path('reset-password/',
				auth_views.PasswordResetView.as_view(template_name="Password_Change/password_reset.html"),name='password_reset'),
		    path('password_reset/done/',
		        auth_views.PasswordResetDoneView.as_view(template_name="Password_Change/password_reset_done.html"),name='password_reset_done'),
		    
		    path('reset-reset-confirm/<uidb64>/<token>/',
		         auth_views.PasswordResetConfirmView.as_view(template_name="Password_Change/password_reset_confirm.html"),name='password_reset_confirm'),
		    path('password-reset-complete/',
		         auth_views.PasswordResetCompleteView.as_view(template_name="Password_Change/password_reset_complete.html"),name='password_reset_complete')


			
			]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
