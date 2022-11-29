from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class AddVacancyPosition(models.Model):
	Name_of_Exam = models.CharField(max_length=100, blank=True,null=True)
	Advertisement = models.CharField(max_length=100, blank=True,null=True)
	Start_Date = models.DateField(blank=True,null=True)
	End_Date = models.DateField(blank=True,null=True)
	Advertisement_Pdf = models.FileField(upload_to='PDF/Advertisement',blank=True,null=True)
	# how many company have open their vacnay
	Vacancy_For_Bhopal = models.BooleanField(default=False,blank=True,null=True)
	Vacancy_For_Indore = models.BooleanField(default=False,blank=True,null=True)
	Vacancy_For_Jabalpur = models.BooleanField(default=False,blank=True,null=True)
	Vacancy_For_Mpgenco = models.BooleanField(default=False,blank=True,null=True)
	Vacancy_For_Mptransco = models.BooleanField(default=False,blank=True,null=True)
	Vacancy_For_Mppmcl = models.BooleanField(default=False,blank=True,null=True)
	# end  

	BHOPAL_Electrical_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	BHOPAL_Electrical_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Electrical_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	BHOPAL_Civil_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Civil_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	BHOPAL_It_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_It_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	BHOPAL_Mechanical_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	BHOPAL_Mechanical_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
# this is for JABLPUR
	JABALPUR_Electrical_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	JABALPUR_Electrical_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Electrical_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	JABALPUR_Civil_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Civil_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	JABALPUR_It_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_It_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	JABALPUR_Mechanical_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	JABALPUR_Mechanical_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
# this is for Indore
	INDORE_Electrical_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	INDORE_Electrical_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Electrical_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	INDORE_Civil_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Civil_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	INDORE_It_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_It_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	INDORE_Mechanical_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	INDORE_Mechanical_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
# this is for MPGENCO
	MPGENCO_ELECTRICAL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPGENCO_ELECTRICAL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_ELECTRICAL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPGENCO_CIVIL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_CIVIL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPGENCO_IT_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_IT_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPGENCO_MECHANICAL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPGENCO_MECHANICAL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
# this is MPTRANSCO
	MPTRANSCO_ELECTRICAL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPTRANSCO_ELECTRICAL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_ELECTRICAL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPTRANSCO_CIVIL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_CIVIL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPTRANSCO_IT_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_IT_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPTRANSCO_MECHANICAL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPTRANSCO_MECHANICAL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	
# this is MPPMCL
	
	MPPMCL_ELECTRICAL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPPMCL_ELECTRICAL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_ELECTRICAL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPPMCL_CIVIL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_CIVIL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPPMCL_IT_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_IT_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_URO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_URF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_STO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_STF = models.PositiveIntegerField(default=0,blank=True,null=True)   
	MPPMCL_MECHANICAL_SCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_SCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_OBCO = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_OBCF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_EWS = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_EWSF = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_PWDHI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_PWDOC = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_PWDVI = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_PWDID = models.PositiveIntegerField(default=0,blank=True,null=True)
	MPPMCL_MECHANICAL_TOTAL = models.PositiveIntegerField(default=0,blank=True,null=True)


class add(models.Model):
	title=models.CharField(max_length=255,default='Enter data')
	sub_title=models.TextField()
	Description=models.TextField(default='add Description')
	title1=models.TextField(default='enter title 1')
	sub_title1=models.TextField(default='enter sub_title 1')
	L1FB_Header=models.TextField(default='enter sub_title 1')
	L1FB_Details=models.TextField(default='enter sub_title 1')
	L1SB_Header=models.TextField(default='enter sub_title 1')
	L1SB_Details=models.TextField(default='enter sub_title 1')
	L2FB_Header=models.TextField(default='enter sub_title 1')
	L2FB_Details=models.TextField(default='enter sub_title 1')
	L2SB_Header=models.TextField(default='enter sub_title 1')
	L2SB_Details=models.TextField(default='enter sub_title 1')
	L3FB_Header=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L3FB_Details=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L3SB_Header=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L3SB_Details=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L4FB_Header=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L4FB_Details=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L4SB_Header=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L4SB_Details=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L5FB_Header=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L5FB_Details=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L5SB_Header=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L5SB_Details=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L6FB_Header=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L6FB_Details=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L6SB_Header=models.TextField(default='enter sub_title 1',null=True,blank=True)
	L6SB_Details=models.TextField(default='enter sub_title 1',null=True,blank=True)
class contact_us(models.Model):
	title=models.CharField(max_length=255,default='title')
	Description=models.TextField(default='Description')
class admin_block(models.Model):
	title=models.CharField(max_length=255)
	By=models.CharField(max_length=255)
	Description=RichTextUploadingField(blank=True,null=True)
	Select_Catogry=models.CharField(max_length=255,default=False)
	Image=models.ImageField(upload_to='media/Images')
	date=models.DateField(auto_now=True)
	status=models.IntegerField(default='1')
	
class footer_data(models.Model):
	Description=models.TextField()
class Banner_data(models.Model):
	Title=models.CharField(max_length=255,default='Add Title here')
	Sub_Title=models.CharField(max_length=255,default='add Sub_Title here')
class Social_Links(models.Model):
	facebook=models.CharField(max_length=255,default='enter facebook link')
	instagram=models.CharField(max_length=255,default='enter instagram link')
	linkedin=models.CharField(max_length=255,default='enter linkedin link')
	twitter=models.CharField(max_length=255,default='enter twitter link')

class Add_category(models.Model):
	category=models.CharField(max_length=255,blank=False)
	create_date=models.DateField(auto_now=True)
class Bussines_content(models.Model):
	title=models.CharField(max_length=255)
	Description=models.TextField()
class Postjobs(models.Model):
	ProjectName=models.CharField(max_length=255)
	CompanyName=models.CharField(max_length=255)
	skills=models.CharField(max_length=255)
	payout=models.CharField(max_length=255)
	Durations=models.CharField(max_length=255)
	Description=models.TextField(default='')
	location=models.CharField(max_length=255,default=True)
	Image=models.ImageField(upload_to='media/Images/Postjobs',blank=True,null=True)
	Date=models.DateField(auto_now=True)

	
class TopFreelancer(models.Model):
	FreelancerName=models.CharField(max_length=255)
	Task=models.CharField(max_length=255)
	city=models.CharField(max_length=255,blank=True)
	collage=models.CharField(max_length=255,blank=True)

