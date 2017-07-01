from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# Create your views here.

#@login_required(login_url='login')
def index(request):
    return render(request, 'welcome.html')

def visit_user(request, visited_username):
    pass