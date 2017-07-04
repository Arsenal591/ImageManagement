from django.shortcuts import render
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MyUser
from .forms import SearchForm


# Create your views here.

@login_required(login_url='login')
def index(request):
    return render(request, 'welcome.html')

@login_required(login_url='login')
def visit_user(request, visited_username):
    pass

@login_required(login_url='login')
def manage_relationship(request, search_result = None):
    search_form = SearchForm(None)
    user = MyUser.objects.get(username=request.user.username)
    followings = user.followings.values()
    blacklist = user.blacklist.values()

    if search_result is not None and len(search_result) == 0:
        messages.info(request, '对不起，找不到该用户！')
    return render(request, 'managerelationship.html', {'search_form': search_form,
                                                       'search_result': search_result, 
                                                       'followings': followings, 
                                                       'blacklist': blacklist,
                                                       'username': request.user.username}
                  )


@login_required(login_url='login')
def follow_user(request, follow_username):
    if request.user.username == follow_username:
        return manage_relationship(request)

    this_user = MyUser.objects.get(username = request.user.username)
    followings = this_user.followings
    if followings.filter(username = follow_username).count()==0:
        that_user = MyUser.objects.get(username=follow_username)
        followings.add(that_user)
        this_user.save()
    else:
        print("sorry this user is already in my followings")

    return manage_relationship(request)

@login_required(login_url='login')
def unfollow_user(request, unfollow_username):
    if request.user.username == unfollow_username:
        return manage_relationship(request)

    this_user = MyUser.objects.get(username = request.user.username)
    followings = this_user.followings

    if followings.filter(username = unfollow_username).count()==1:
        that_user = MyUser.objects.get(username=unfollow_username)
        followings.remove(that_user)
        this_user.save()
    else:
        print("sorry i haven NOT followed this user")
    return manage_relationship(request)

@login_required(login_url='login')
def black_user(request, black_username):
    if request.user.username == black_username:
        return manage_relationship(request)

    this_user = MyUser.objects.get(username = request.user.username)
    blacklist = this_user.blacklist

    if blacklist.filter(username = black_username).count()==0:
        that_user = MyUser.objects.get(username=black_username)
        blacklist.add(that_user)
        this_user.save()
    else:
        print("sorry already in my blacklist")

    return manage_relationship(request)


@login_required(login_url='login')
def unblack_user(request, unblack_username):
    if request.user.username == unblack_username:
        return manage_relationship(request)

    this_user = MyUser.objects.get(username = request.user.username)
    blacklist = this_user.blacklist

    if blacklist.filter(username = unblack_username).count()==1:
        that_user = MyUser.objects.get(username=unblack_username)
        blacklist.remove(that_user)
        this_user.save()
    else:
        print("sorry NOT in my blacklist")

    return manage_relationship(request)

@login_required(login_url='login')
def search_user(request):
    params = request.POST if request.method == 'POST' else None
    form = SearchForm(params)

    if form.is_valid():
        username = form.cleaned_data['username']
        results = MyUser.objects.filter(username=username)
        return manage_relationship(request, results)
    else:
        messages.info(request, '您的输入不合法！')
        return manage_relationship(request)

