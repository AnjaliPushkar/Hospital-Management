from django.contrib import auth
from django.shortcuts import render

def home(request):
    return render(request, 'home1.html')

def validate(request):
    return render(request, 'Validate.html')

def appointment(request):
    return render(request, 'appointment.html')
