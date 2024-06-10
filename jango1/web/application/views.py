
from django.shortcuts import render,redirect
from .forms import *
from .models import *
# Create your views here.


def index(request):
    return render(request,'index.html')

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
    return render(request,'admin.html')
