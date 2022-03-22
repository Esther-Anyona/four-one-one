from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import *
from django.contrib.auth.models import User


"""
Views here
"""
def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'home.html', {'neighbourhoods':neighbourhoods})
