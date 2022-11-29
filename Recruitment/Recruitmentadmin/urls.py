from django.urls import path
from . import views
from django.conf.urls.static import  static
from django.conf import settings
urlpatterns=[path('',views.home),
				# path('about_us/<int:id>',views.About_us, name='About_us'),
				path('',views.home, name='home'),
				path('openings/',views.Opening, name='Opening'),
				path('view/openings/<int:id>',views.View_Openings,name='View_Openings'),
				path('All_Openings/',views.All_Openings,name='All_Openings'),
				path('DataDelete/<int:id>',views.HandleDelete,name='HandleDelete'),

				path('login/',views.handlelogin,name='handlelogin'),
				path('logout/',views.logout,name='logout'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)