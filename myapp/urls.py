from django.contrib import admin
from django.urls import path 
from myapp import views
admin.site.site_header = " Admin Page"
admin.site.site_title = " Admin Portal"
admin.site.index_title = "Welcome to SARTHI's database Portal"
urlpatterns = [

path("",views.index,name='index'),
path("about.html",views.about,name='about'),
path("contact.html",views.contact,name='contact'),
path("package.html",views.package,name='package'),
path("service.html",views.service,name='service'),
path("weather.html",views.weather,name='weather'),
path("curr.html",views.curr,name='currency conv'),

# path("service",views.service,name='service'),
# path("contact",views.contact,name='contact'),

]