
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *
# Create your views here.


def index(request):
    if request.user.is_anonymous :
        return redirect("/login")
    return render(request,'index.html')

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('login') 


def patient(request):
    form =Blood.objects.all()
    context ={'form':form}
    return render(request, 'patient.html',context)


def services(request):
    return render(request,'services.html')


def donor(request):
    f=Donor.objects.all()
    context ={'f':f}
    return render(request, 'donor.html',context)


def admin(request):
    if request.method=="POST":
        username=request.POST.get("name")
        password=request.POST.get("password")

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
