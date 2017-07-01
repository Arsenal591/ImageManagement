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
from .forms import *
from .slave import *
from scipy import misc
from django.http import HttpResponse
from django.conf import settings

def img_pool(request):
    imgs = ImagePost.objects.order_by('-created_at')
    pub_imgs = [img for img in imgs if img.is_public]
    pub_imgs = pub_imgs[:6]
    return render(request, 'pool.html', {'imgs': pub_imgs})

def upload(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if True: # lazy to delete this line
            post = form.save(commit=False)
            # need to add user info here
            post.save()
            return redirect('process', post.id)
    return render(request, 'upload.html', {'form': UploadForm()})

def create_img(img_post, method, **kwargs):
    new_post = ImagePost()

    img_dir = os.getcwd() + '/images/' + settings.MEDIA_DIR
    img_name = str(img_post.img)
    img_file = misc.imread(img_dir + img_name)

    new_img = gray(img_file)
    if method == 'gray':
         new_img = gray(img_file) 
    new_path = img_dir + img_name.split('.')[0] + '_' + method + '.jpg'
    misc.imsave(new_path, new_img)

    new_post.img = File(new_path)
    new_post.author = img_post.author
    new_post.is_public = img_post.is_public
    new_post.parent = img_post
    for tag in img_post.tags.all():
        new_post.tags.add(tag)
    new_post.save()

def process(request, img_id):
    img_post = get_object_or_404(ImagePost, pk=img_id)
    form = ProcessForm(request.POST)
    if form.is_valid():
        if form['gray']:
            create_img(img_post, 'gray')
#        if form['blur'] != 0:
#            create_img(img_post, 'blur', degree=form['blur'])
        return render(request, 'success.html')
        # if form.binaryzation
            
    
    return render(request, 'process.html', {'img': img_post, 'form': ProcessForm()})
        

