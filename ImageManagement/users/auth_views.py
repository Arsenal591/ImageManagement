from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import LoginForm, SignupForm, ChangeinfoForm

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
        messages.info(request, '用户名或密码错误！')
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
        form.save()
        return redirect('login')
    return redirect('signup')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

@login_required(login_url='login')
def changepassword(request):
    change_password_form = auth.forms.PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {'form':change_password_form})

@login_required(login_url='login')
def changepassword_submit(request):
    params = request.POST if request.method == 'POST' else None
    form = auth.forms.PasswordChangeForm(request.user, params)

    if form.is_valid():
        user = form.save()
        auth.update_session_auth_hash(request, user)
        return redirect('login')
    else:
        return redirect('changepassword')

@login_required(login_url='login')
def changeinfo(request):
    form = ChangeinfoForm(None)
    return render(request, 'changeinfo.html', {'form':form})

@login_required(login_url='login')
def changeinfo_submit(request):
    params = request.POST if request.method == 'POST' else None
    form = ChangeinfoForm(params)
    form.set_username(request.user.username)

    if form.is_valid():
        form.save()
        return redirect('/')
    else:
        return redirect('changeinfo')