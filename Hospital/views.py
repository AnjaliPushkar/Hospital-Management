from django.contrib import auth
from django.shortcuts import render

def home(request):
    return render(request, 'home1.html')

def validate(request):
    return render(request, 'Validate.html')

def appointment(request):
    return render(request, 'appointment.html')

def staffsSignup(request):
    return render(request, 'staffsSignup.html')

def staffsLogin(request):
    return render(request, 'staffsLogin.html')

def Users_Login(request):
    return render(request, 'Users-Login.html')

def Users_signup(request):
    return render(request, 'Users-signup.html')
