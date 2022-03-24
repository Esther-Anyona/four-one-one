from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *


"""
Views here
"""
@login_required(login_url='Login')
def home(request):
    neighbourhoods = Neighbourhood.objects.all()
    return render(request, 'home.html', {'neighbourhoods':neighbourhoods})

@login_required(login_url='Login')
def profile(request, username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(user = profile.id)
    return render(request, 'profile.html', {'profile':profile, 'profile_details':profile_details})

@login_required(login_url='Login')
def Logout(request):
    logout(request)
    return redirect('home')



def register(request):
    if request.method == 'POST':
        context = {'has_error': False}
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords Do Not Match! Try Again')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exists! Choose Another One')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Address Already Exists! Choose Another One')
            return redirect('register')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.is_active = False
        user.save()

        if not context['has_error']:
            send_activation_email(user, request)
            messages.success(request, 'Registration is successful!')
            return redirect('register')

    return render(request, 'registration/registration_form.html')


@login_required(login_url='/accounts/login/')
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('edit_profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile.html', context)

def search(request):
    if request.method == 'POST':
        search = request.POST['Search Business']
        print(search)
        businesses = Business.objects.filter(name__icontains = search).all()
        return render(request, 'search_results.html', {'search':search, 'businesses':businesses})
    else:
        return render(request, 'search_results.html')


