from django.contrib import admin
from django.urls import path,include
from home import views 
urlpatterns = [
    
    path('', views.index, name="index"),
    path('login', login.index, name="login"),
    path('logout', logout.index, name="logout"),
]