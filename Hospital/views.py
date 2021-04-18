from django.contrib import auth
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
