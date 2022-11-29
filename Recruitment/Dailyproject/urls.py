from django.contrib import admin
from django.urls import path ,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Recuritment/admin/',include('Recruitmentadmin.urls')),
    path('ckeditor/',include('ckeditor_uploader.urls')),
    path('',include('Applicant.urls')),
]+static(settings.MEDIA_URL,doucment_root=settings.MEDIA_ROOT)
