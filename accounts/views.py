from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from .forms import MyRegistrationForm, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.http import JsonResponse
from django.core import serializers
from json import loads as json_loads
from django.core.paginator import Paginator
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()
# User = settings.AUTH_USER_MODEL


def signin(request):
    next = request.GET.get('next')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                if next:
                    return redirect(next)
                else:
                    if request.user.admin:
                        return redirect('/admin')
                    else: 
                        return redirect("/")
        else:
            messages.error(request,"Oops! That didn't work. Please check your email and password and try again")
    else:
            form = AuthenticationForm(request.POST)
    if request.user.is_authenticated:
        return redirect('/')
    else:
        context = {
            'form': form,
            'next':next,
            'email': request.POST.get('email'),
            'title': 'Sign In ' + '| ' + settings.SITE_NAME,
        }
        return render(request, 'accounts/signin.html', context)


def signup(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            login(request, user)
            next = request.GET.get("next")
            if next:
                return redirect(next)
            else:
                return redirect('/')
    else:
        form = MyRegistrationForm()
                
    if request.user.is_authenticated:
        return redirect('/')
    else:
        context = {
            'title': 'Sign Up ' + '| ' + settings.SITE_NAME,
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'email': request.POST.get('email'),
            'zip_code': request.POST.get('zip_code'),
            'phone_number': request.POST.get('phone_number'),
            'form': form,
        }
        return render(request, 'accounts/signup.html', context)


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('/profile/' + request.user.email)
        else:
            messages.error(request, 'Please correct the error below')
    else:
        form = PasswordChangeForm(request.user)

    context = {
        'title': 'Change Password ' + '| ' + settings.SITE_NAME,
        'form':form,
    }
    return render(request, 'accounts/change_password.html', context)
