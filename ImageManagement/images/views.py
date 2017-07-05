from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User
import time
import os
import random
from .forms import *
from .slave import *
from .master import *
#from users import MyUser
#from timeline import timeline_spread as ts
from scipy import misc
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from timeline.timeline_spread import *
from users.models import MyUser

def home(request):
    return render(request, 'home.html')
def img_pool(request):
    pub_imgs = ImagePost.objects.filter(is_public=True).order_by('-created_at')
    return render(request, 'pool.html', {'imgs':pub_imgs[:30]})
#    row1 = pub_imgs[:6]
#    row2 = pub_imgs[6:12]
#    row3 = pub_imgs[12:18]
#    return render(request, 'pool.html', {'row1':row1, 'row2':row2, 'row3':row3})

def add_tag(post, tag_line):
    tags = tag_line.split()
    for tag in tags:
        tag = tag.lower()
        tag_ins = None
        tag_set = ImageTag.objects.filter(name=tag)
        if tag_set:
            tag_ins = tag_set[0]
        else:
            tag_ins = ImageTag(name=tag)
            tag_ins.save()
        post.tags.add(tag_ins)

@login_required
def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if True: # lazy to delete this line
            find_user = MyUser.objects.get(username=request.user.username)
            post = form.save()
            post.author = find_user
            add_tag(post, form['tags'].value())
            is_public = bool(form['is_public'].value())
            # need to add user info here
            post.save()
            create_post_timeline(find_user, post)
            return redirect('process', post.id)
    return render(request, 'upload.html', {'form': UploadForm()})

def create_post_entry(is_public, description, img, tags, author):
    new_post = ImagePost()
    new_post.save()
    new_post.img = img
    new_post.is_public = is_public
    new_post.description = description
    add_tag(new_post, tags)
    new_post.author = author
    new_post.save()

@login_required
def upload_batch(request):
    if request.method == 'POST':
        form = BatchUploadForm(request.POST)
        if True: # lazy to delete this line
            is_public = bool(form['is_public'].value())
            description = form['description'].value()
            tags = form['tags'].value()
            imgs = request.FILES.getlist('img_batch')
            for img in imgs:
                create_post_entry(is_public, description, img, tags, request.user)
                find_user = MyUser.objects.get(username=request.user.username)
                create_post_timeline(find_user, post)
            return home(request)
    return render(request, 'upload_batch.html', {'form': BatchUploadForm()})

def create_img(img_post, method, **kwargs):
    img_dir = os.getcwd() + '/images/' + settings.MEDIA_DIR
    img_name = str(img_post.img)
    img_file = misc.imread(img_dir + img_name)

    new_img = None
    if method == 'gray':
        new_img = gray(img_file) 
    elif method == 'blur':
        new_img = blur(img_file, kwargs['degree'])
    elif method == 'binary':
        new_img = binaryzation(img_file)
    elif method == 'rescale':
        new_img = rescale(img_file, kwargs['percentage'])
    elif method == 'rotate':
        new_img = rotate(img_file, kwargs['angle'])
    else:
        return
    new_name = img_name.split('.')[0] + '_' + method + str(random.randint(0,1000)) + '.jpg'
    new_path = img_dir + new_name
    misc.imsave(new_path, new_img)

    new_post = ImagePost()
    new_post.save()
    new_post.img.name = new_name
    new_post.author = img_post.author
    new_post.is_public = img_post.is_public
    new_post.parent = img_post
    new_post.description = img_post.description
    for tag in img_post.tags.all():
        new_post.tags.add(tag)
    new_post.save()

@login_required
def process(request, img_id):
    img_post = get_object_or_404(ImagePost, pk=img_id)
    form = ProcessForm(request.POST)
    if request.method=='POST' and form.is_valid():

        if bool(form['gray'].value()):
            create_img(img_post, 'gray')
        
        if bool(form['to_blur'].value()):
            blur = form['blur'].value()
            if len(blur) != 0:
                blur = float(blur)
                create_img(img_post, 'blur', degree=blur)
        
        if bool(form['binaryzation'].value()):
            create_img(img_post, 'binary')
        
        if bool(form['to_rescale'].value()):
            percent = float(form['rescale'].value())
            # for convience set the height and width percentage the same
            create_img(img_post, 'rescale', percentage=[percent, percent])
        
        if bool(form['to_rotate'].value()):
            rotate = form['rotate'].value()
            if len(rotate) != 0:
                rotate = int(rotate)
                if rotate != 0 and rotate != 360:
                    create_img(img_post, 'rotate', angle=rotate)
        
        return home(request)

    return render(request, 'process.html', {'img': img_post, 'form': ProcessForm()})

@login_required
def detail(request, img_id):
    img_post = get_object_or_404(ImagePost, pk=img_id)
    relatives = []
#    It's said the ImagePost doesn't have attribute 'parent_set', that's strange
#    relatives = img_post.parent_set.all()
#    if img_post.parent != None:
#        relatives.union(img_post.parent.parent_set.all())
    if request.method == 'POST':
        form = DetailForm(request.POST)
        # things about timeline
    return render(request, 'detail.html', {'img': img_post, 'relatives': relatives, 'form': DetailForm()})

def filtershow(request):
    form = FilterForm(request.POST)
    img_set = None
    user = None
    info = ''
    if form.is_valid():
        is_pub = None
       
        if form['user_filter'].value() == 'Mine':
            user = request.user
            info += 'My images'
        elif form['user_filter'].value() == 'All':
            user = None
            info += 'All public images'
        else:
            try:
                user = User.objects.get(
                  username=form['username'].value()
                )
                info += "%s's images"
            except Exception as e:
                return render(request, 'filter.html', {'imgs': img_set, 'form': FilterForm(), 'info': 'Not found specified user'})

        if user == None:
            img_set = ImagePost.objects.all()
        else:
            img_set = ImagePost.objects.filter(author=user)

        if form['auth_filter'].value() == 'Public':
            is_pub = True
        elif form['auth_filter'].value() == 'Private':
            is_pub = False
        else:
            pass
        
        if user == request.user:
            if is_pub != None:
                img_set = img_set.filter(is_public=is_pub)
        else:
            img_set = img_set.filter(is_public=True)

        tags = form['tags'].value()
        if len(tags) != 0:
            info += ', tags: %s' % tags
            tags = tags.split()
            # Trying to query the posts that have at least on of the tags
            # We can also query the posts with all the tags, but I don't like it
            # Can be discussed later, if necessary
            img_set = img_set.filter(tags__name__in=tags)

        if bool(form['between_date'].value()):
            img_set = img_set.filter(created_at__range=(form['date_start'].value(), form['date_end'].value()))
        

        return render(request, 'filter.html', {'imgs': img_set, 'form': FilterForm(), 'info': info})
     
    return render(request, 'filter.html', {'imgs': img_set, 'form': FilterForm(), 'info': info})


def pic(request, pic_id):
    pic = get_object_or_404(ImagePost, pk=pic_id)
    return render(request, 'pic.html', {'img': pic})

# search image by given image
# It's not quite decent to use this function name
# but search_by_image will raise an error and I don't know why
def searchimg(request):
    '''Simple and dirty method: auto-tag the image, and search imgs with same tags'''
    tags = None
    info = 'All public images, tags: '
    if request.method == 'POST':
        src_img = misc.imread(request.FILES['img'])
        # it's meaningless to try to unserstand detail operations below =)
        # just know the tags are the tags
        raw_tags = recognize(src_img)[0]
        tags = []
        img_set = None
        for bag in raw_tags:
            # info += bag[0]
            if True:
                try:
                    tag_instance = TagNo.objects.get(no=bag[0]).tag
                    if tag_instance not in tags:
                        tags.append(tag_instance)
                        info += '%s ' % tag_instance.name
                except Exception as e:
                    print(e)
                    pass
        if len(tags) != 0:
            img_set = ImagePost.objects.filter(tags__in=tags)
        else:
            pass
        return render(request, 'filter.html', {'imgs': img_set, 'form': FilterForm(), 'info': info})
        
    return render(request, 'img_srch.html', {'tags': tags, 'form': ImgSrchForm()})


# the search in the navi-bar
def searchbar(request):
    # can't be None, because None can't be iterated
    img_set = []
    info = ''
    if request.method == 'POST':
        keywords = request.POST['keywords'].split()
        img_set = ImagePost.objects.filter(tags__name__in=keywords)
        for keyword in keywords:
            try:
                user = User.objects.get(username=keyword)
                img_set = img_set.union(ImagePost.objects.filter(author=user, is_public=True))
                # img_set = ImagePost.objects.filter(author=user)
            except Exception as e:
                pass
        info = 'search keywords: %s' % request.POST['keywords']
    return render(request, 'filter.html', {'imgs': img_set, 'form': FilterForm(), 'info': info})




















