from django.contrib import admin
from .models import *
import csv
# Register your models here.
admin.site.register(userprofile)
# admin.site.register(PersonalDetail)
# admin.site.register(OtherDetail)

# Education Details
# class EducationDetailsAdmin(admin.ModelAdmin):
	# list_display= ('HSC_SUBJECT','HSSC_SUBJECT','GRADUATION_SUBJECT','POST_GRADUATION_SUBJECT')

# admin.site.register(EducationDetails, EducationDetailsAdmin)

admin.site.register(EducationDetails)
# personal details 
class PersonalDetailAdmin(admin.ModelAdmin):
	list_display= ('FIRST_NAME','LAST_NAME', 'GATE_SCORE', )

admin.site.register(PersonalDetail, PersonalDetailAdmin)

# other deatils
class OtherDetailAdmin(admin.ModelAdmin):
    list_display= ('NATIVE_OF_MADHYA_PRADESH', 'CATEGORY', 'BELONGS_TO_CREAMY_LAYER', 'DISABILITY_CERTIFICATE')
    
  
admin.site.register(OtherDetail, OtherDetailAdmin)

admin.site.register(AddressDetail)
admin.site.register(BankDetail)
admin.site.register(DocumentUpload)
admin.site.register(ChoiceFilling)
admin.site.register(FinalDataTable)
admin.site.register(PaymentDetail)
admin.site.register(FlagDetail)
# @admin.register(FinalDataTable)
# class VillainAdmin(admin.ModelAdmin, ExportCsvMixin):
#     ...
#     readonly_fields = ["USER_CODE"]