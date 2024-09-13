from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request, 'home.html', {})

def login_user(request):
    pass

def logut_user(request):
    pass
