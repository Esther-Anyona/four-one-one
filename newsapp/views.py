from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

"""
Views here
"""
def home(request):
    return render(request, 'home.html')
