from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Contact
from django.contrib import messages

def index(request):

    return render(request,"index.html")
###########

def about(request):

    return render(request,"about.html")
###########

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        subject= request.POST.get('subject')
        desc= request.POST.get('desc')
        contact=Contact(name=name, email=email,subject=subject,desc= desc,date=datetime.today())
        contact.save()
        messages.success(request, "form subitted succesfully.")
    return render(request,"contact.html")
###########

def service(request):

    return render(request,"service.html")
##########

def package(request):

    return render(request,"package.html")


    
