from django.shortcuts import render,redirect
from .forms import UserLoginForm,UserRegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User
# Create your views here


def login_user(request):
    if request.method=='POST':
        form=UserLoginForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,email=cd['email'],password=cd['password'])
            if user:
                login(request,user)
                messages.success(request,'you loged in successfully','success')
                return redirect('shop:home')
            else:
                messages.error(request,'user name or password was wrong','danger')
    else:
        form=UserLoginForm()
    return render(request,'accounts/login.html',{'form':form})


def logout_user(request):
    logout(request)
    messages.success(request,'you logged out successfully','success')
    return redirect('shop:home')

def sign_up(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=User.objects.create_user(email=cd['email'],full_name=cd['full_name'],password=cd['password'])
            user.save()
            messages.success(request,'you sign up successfully','success')
            return redirect('shop:home')
    else:
        form= UserRegisterForm()
    return render(request,'accounts/signup.html',{'form':form})
