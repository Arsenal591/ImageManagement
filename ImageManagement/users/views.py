from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import MyUser
from .forms import SearchForm
from images.models import ImagePost
from timeline.models import Timeline
from timeline.timeline_generator import *
from timeline.timeline_spread import *
from timeline.timeline_analysis import *


# Create your views here.

@login_required(login_url='login')
def index(request):
    user = MyUser.objects.get(username=request.user.username)
    imgs = ImagePost.objects.filter(author__username=request.user.username).values()
    timelines = select_subject_timeline_by_user(user).values()
    followings = user.followings.values()
    followers = user.followers.values()
    blocks = user.blacklist.values()
    collection = get_image_collection(user).values()

    return render(request, 'welcome.html', {'user':user,
                                            'imgs':imgs,
                                            'timelines':timelines,
                                            'followings':followings,
                                            'followers':followers,
                                            'blocks':blocks,
                                            'collection':collection})

@login_required(login_url='login')
def visit_user(request, visited_username):
    user = MyUser.objects.get(username=visited_username)
    imgs = ImagePost.objects.filter(author__username=request.user.username).values()
    timelines = get_object_timeline_by_name(request.user.username, visited_username)
    followings = user.followings.values()
    followers = user.followers.values()
    collection = get_image_collection(user).values()

    return render(request, 'userinfo.html', {'user':user,
                                            'imgs':imgs,
                                            'timelines':timelines,
                                            'followings':followings,
                                            'followers':followers,
                                            'collection':collection})
@login_required(login_url='login')
def profile(request):
    user = MyUser.objects.get(username=request.user.username)
    imgs = ImagePost.objects.filter(author__username=request.user.username).values()
    timelines = select_object_timeline_by_user(user, user).values()
    followings = user.followings.values()
    followers = user.followers.values()
    blocks = user.blacklist.values()
    collection = get_image_collection(user).values()

    return render(request, 'userinfo.html', {'user':user,
                                            'imgs':imgs,
                                            'timelines':timelines,
                                            'followings':followings,
                                            'followers':followers,
                                            'blocks':blocks,
                                            'collection':collection})

@login_required(login_url='login')
def manage_relationship(request, search_result = None):
    search_form = SearchForm(None)
    user = MyUser.objects.get(username=request.user.username)
    followings = user.followings.all()
    blacklist = user.blacklist.all()

    if search_result is not None and len(search_result) == 0:
        messages.info(request, 'User not found!')
    return render(request, 'managerelationship.html', {'search_form': search_form,
                                                       'search_result': search_result, 
                                                       'followings': followings, 
                                                       'blacklist': blacklist,
                                                       'username': request.user.username}
                  )


@login_required(login_url='login')
def follow_user(request, follow_username, url):
    url = '/index/' + url
    if request.user.username == follow_username:
        return manage_relationship(request)

    this_user = MyUser.objects.get(username = request.user.username)
    followings = this_user.followings
    if followings.filter(username = follow_username).count()==0:
        that_user = MyUser.objects.get(username=follow_username)
        followings.add(that_user)
        this_user.save()
    else:
        messages.info(request,"sorry this user is already in my followings")
    return redirect(url)
    return redirect('manage-relationship')

@login_required(login_url='login')
def unfollow_user(request, unfollow_username, url):
    url = '/index/' + url
    if request.user.username == unfollow_username:
        return manage_relationship(request)

    this_user = MyUser.objects.get(username = request.user.username)
    followings = this_user.followings

    if followings.filter(username = unfollow_username).count()==1:
        that_user = MyUser.objects.get(username=unfollow_username)
        followings.remove(that_user)
        this_user.save()
    else:
        messages.info(request, "sorry you haven NOT followed this user")
    return redirect(url)
    return redirect('manage-relationship')

@login_required(login_url='login')
def black_user(request, black_username, url):
    url = '/index/' + url
    if request.user.username == black_username:
        return manage_relationship(request)

    this_user = MyUser.objects.get(username = request.user.username)
    blacklist = this_user.blacklist

    if blacklist.filter(username = black_username).count()==0:
        that_user = MyUser.objects.get(username=black_username)
        blacklist.add(that_user)
        this_user.save()
    else:
        messages.info(request, "sorry already in your blacklist")

    return redirect(url)
    #return redirect('manage-relationship')

@login_required(login_url='login')
def unblack_user(request, unblack_username, url):
    url = '/index/' + url
    if request.user.username == unblack_username:
        return manage_relationship(request)

    this_user = MyUser.objects.get(username = request.user.username)
    blacklist = this_user.blacklist

    if blacklist.filter(username = unblack_username).count()==1:
        that_user = MyUser.objects.get(username=unblack_username)
        blacklist.remove(that_user)
        this_user.save()
    else:
        messages.info(request,"sorry NOT in my blacklist")

    return redirect(url)
    return redirect('manage-relationship')


@login_required(login_url='login')
def search_user(request):
    params = request.POST if request.method == 'POST' else None
    if params is None:
        return manage_relationship(request)
    form = SearchForm(params)

    if form.is_valid():
        username = form.cleaned_data['username']
        results = MyUser.objects.filter(username=username)
        redirect('manage-relationship')
        return manage_relationship(request, results)
    else:
        messages.info(request, 'Invalid input!')
        #redirect('manage-relationship')
        return manage_relationship(request)

def like(request, timeline_id, url):
    user = MyUser.objects.get(username=request.user.username)
    timeline = Timeline.objects.get(id=timeline_id)
    create_like_timeline(user, timeline)
    redirect(url)
    
def collect(request, timeline_id, url):
    user = MyUser.objects.get(username=request.user.username)
    timeline = Timeline.objects.get(id=timeline_id)
    create_collect_timeline(user, timeline)
    redirect(url)

def comment(request, timeline_id, url):
    user = MyUser.objects.get(username=request.user.username)
    timeline = Timeline.objects.get(id=timeline_id)
    comment = request.POST['comment']
    create_collect_timeline(user, timeline, comment)
    redirect(url)
