from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from newapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^newsletter/$', views.newsletter),
    url(r'^courses/$', views.courses),
    url(r'^python/$', views.python),
	url(r'^api/$', views.api),
	url(r'^html/$', views.html),
	url(r'^sucess/$', views.sucess),
	url(r'^search/$', views.search),
    
]

