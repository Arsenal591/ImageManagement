from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm

def login(request):
    login_form = LoginForm(None)
    return render(request, 'login.html', {'login_form': login_form})

def authenticate(request):
    params = request.POST if request.method == 'POST' else None
    form = LoginForm(params)
    
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(request, username=username, password=password)
    if not user:
        return redirect('login')
    auth.login(request, user)
    return redirect('index')

def signup(request):
    signup_form = SignupForm(None)
    return render(request, 'signup.html', {'signup_form': signup_form})

def signup_submit(request):
    params = request.POST if request.method == 'POST' else None
    form = SignupForm(params)
    if form.is_valid():
        print('Im valid')
        new_user = form.save(commit=False)
        new_user.email = form.cleaned_data['email']
        new_user.nickname = form.cleaned_data['nickname']
        new_user.gender = form.cleaned_data['gender']
        new_user.save()
        return redirect('login')
    print('Im dirty', form)
    return redirect('signup')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

