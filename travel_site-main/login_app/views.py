from django.shortcuts import render

def index(request):

    return render(request,"index.html")
# Create your views here.
def login(request):

    return render(request,"login.html")

def logout(request):

    return render(request,"index.html")