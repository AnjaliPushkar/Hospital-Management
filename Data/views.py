from django.shortcuts import render, redirect, get_object_or_404
from .models import vaccinated
from django.contrib.auth.models import User, auth
from django.contrib import auth
# Create your views here.
def doctor(request):
    return render(request, 'Data/doctor.html')

def check(request):
    return render(request, 'Data/check.html')

def add(request):
    if request.method == "POST":
        if request.POST['name'] and request.POST['adhar'] and request.POST['mobile'] and request.POST['dob']:
            table = vaccinated()
            table.name = request.POST['name']
            table.adhar = request.POST['adhar']
            table.mobile = request.POST['mobile']
            table.dob = request.POST['dob']
            # table.pic = request.FILES['pic']
            table.save()
            
            return redirect('/Data/', str(table.id))
        else:
            return render(request, 'Data/add.html')
    else:
        return render(request, 'Data/add.html')
