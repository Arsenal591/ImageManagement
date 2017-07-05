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

def get_timeline_details(user, timelines):
    result = list()
    for timeline in timelines:
        data = dict()
        data['id'] = timeline.id
        data['type'] = timeline.type
        data['sender_id'] = timeline.sender_id
        data['image_id'] = timeline.image_id
        data['receiver_id'] = timeline.receiver_id
        data['occur_time'] = timeline.occur_time
        data['comment_text'] = timeline.comment_text
        data['if_liked'] = (Timeline.objects.filter(sender_id__username=user.username, type='like', image_id=timeline.image_id).count() > 0)
        data['if_collected'] = (Timeline.objects.filter(sender_id__username=user.username, type='collect', image_id=timeline.image_id).count() > 0)
        result.append(data)
    return result

@login_required(login_url='login')
def index(request):
    user = MyUser.objects.get(username=request.user.username)
    imgs = ImagePost.objects.filter(author__username=request.user.username).all()
    timelines = select_subject_timeline_by_user(user)
    timelines = get_timeline_details(user, timelines)
    followings = user.followings.all()
    followers = user.followers.all()
    blocks = user.blacklist.all()
    collection = get_image_collection(user).all()

    return render(request, 'welcome.html', {'user':user,
                                            'imgs':imgs,
                                            'timelines':timelines,
                                            'followings':followings,
                                            'followers':followers,
                                            'blocks':blocks,
                                            'collection':collection})

@login_required(login_url='login')
def visit_user(request, visited_username):
    this_user = MyUser.objects.get(username=request.user.username)
    visit_user = MyUser.objects.get(username=visited_username)

    timelines = get_object_timeline_by_user(request.user.username, visited_username)
    timelines = get_timeline_details(this_user, timelines)
    imgs = ImagePost.objects.filter(author__username=request.user.username, image_id__is_public=1).all()
    followings = user.followings.all()
    followers = user.followers.all()
    collection = get_image_collection(user).all()

    if_following = visit_user in this_user.followings.all()
    if_blocked = visit_user in this_user.blacklist.all()
    hidden = if_blocked or this_user in visit_user.blacklist.all()

    return render(request, 'userinfo.html', {'user':visit_user,
                                             'if_following':if_following,
                                             'if_blocked':if_blocked,
                                             'hidden':hidden,
                                             'imgs':imgs,
                                             'timelines':timelines,
                                             'followings':followings,
                                             'followers':followers,
                                             'collection':collection})
@login_required(login_url='login')
def profile(request):
    user = MyUser.objects.get(username=request.user.username)
    imgs = ImagePost.objects.filter(author__username=request.user.username).all()
    timelines = select_object_timeline_by_user(user, user)
    timelines = get_timeline_details(user, timelines)
    followings = user.followings.all()
    followers = user.followers.all()
    blocks = user.blacklist.all()
    collection = get_image_collection(user).all()

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

def unlike(request, timeline_id, url):
    user = MyUser.objects.get(username=request.user.username)
    this_timeline = Timeline.objects.get(id=timeline_id)
    target_timeline = Timeline.objects.get(image_id=this_timeline.image_id, type='like')
    target_timeline.delete()
    redirect(url)

def uncollect(request, timeline_id, url):
    user = MyUser.objects.get(username=request.user.username)
    this_timeline = Timeline.objects.get(id=timeline_id)
    target_timeline = Timeline.objects.get(image_id=this_timeline.image_id, type='collect')
    target_timeline.delete()
    redirect(url)