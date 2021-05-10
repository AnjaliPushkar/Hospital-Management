from django.shortcuts import render, redirect, get_object_or_404
# from .models import A_data
from django.contrib.auth.models import User, auth
from django.contrib import auth
# Create your views here.
def doctor(request):
    return render(request, 'Data/doctor.html')
