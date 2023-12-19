from django.contrib import admin
from django.urls import path 
from myapp import views
admin.site.site_header = "Vishesh's Admin"
admin.site.site_title = "Vishesh's Admin Portal"
admin.site.index_title = "Welcome to Vishesh's Researcher Portal"
urlpatterns = [

path("",views.index,name='index'),
path("about.html",views.about,name='about'),
path("contact.html",views.contact,name='contact'),
path("package.html",views.package,name='package'),
path("service.html",views.service,name='service'),
path("blog.html",views.blog,name='Blogs'),

# path("service",views.service,name='service'),
# path("contact",views.contact,name='contact'),

]