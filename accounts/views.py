from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import SignupForm
# Create your views here.

def signup_view(request):
    if request.method=="POST":
        form=SignupForm(request.POST)
        if form.is_valid():
           user=form.save()
           login(request,user)
           return redirect('home')
    else:
        form=SignupForm()
    return render(request, 'signup.html', {'form':form})

def login_view(request):
    if request.method=="POST":
        form=AuthenticationForm(request.POST)
        if form.is_valid():
           username=form.cleaned_data.get("username")
           password=form.cleaned_data.get("password")
           user=authenticate(request=request, username=username, password=password)
           if user is not None:
               login(request, user)
               return redirect('home')
    else:
        form=AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('home')