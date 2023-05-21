import re
from django.utils.timezone import datetime

from django.shortcuts import render 

from django.http import HttpResponse

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def login(request):
    return render(request,'hello/login.html')

def infra(request):
    return render(request,'hello/infra.html')

def joinmember(request):
    return render(request,'hello/joinmember.html')




