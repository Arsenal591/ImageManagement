from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import ImageTag, ImagePost
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.core.files import File
import time
import os
import random
from .forms import *
from .slave import *
from scipy import misc
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

def img_pool(request):
    imgs = ImagePost.objects.order_by('-created_at')
    pub_imgs = [img for img in imgs if img.is_public]
    pub_imgs = pub_imgs[:6]
    return render(request, 'pool.html', {'imgs': pub_imgs})

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
            post = form.save()
            post.author = request.user
            add_tag(post, form['tags'].value())
            # need to add user info here
            post.save()
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
            is_public = bool(form['description'].value())
            description = form['description'].value()
            tags = form['tags'].value()
            imgs = request.FILES.getlist('img_batch')
            for img in imgs:
                create_post_entry(is_public, description, img, tags, request.user)
            return render(request, 'success.html')
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
    if form.is_valid():

        if bool(form['gray'].value()):
            create_img(img_post, 'gray')
        
        blur = form['blur'].value()
        if len(blur) != 0:
            blur = float(blur)
            create_img(img_post, 'blur', degree=blur)
        
        if bool(form['binaryzation'].value()):
            create_img(img_post, 'binary')
        
        percent = float(form['rescale'].value())
        if percent != 1:
            # for convience set the height and width percentage the same
            create_img(img_post, 'rescale', percentage=[percent, percent])
        
        rotate = form['rotate'].value()
        if len(rotate) != 0:
            rotate = int(rotate)
            if rotate != 0 and rotate != 360:
                create_img(img_post, 'rotate', angle=rotate)
        
        return render(request, 'success.html')

    return render(request, 'process.html', {'img': img_post, 'form': ProcessForm()})
        
def filtershow(request):
    return render(request, 'filter.html')

def home(request):
    return render(request, 'home.html')
