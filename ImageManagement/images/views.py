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
    pub_imgs = pub_imgs[:]
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
    new_path = img_dir + img_name.split('.')[0] + '_' + method + '.jpg'
    misc.imsave(new_path, new_img)

    new_post = ImagePost()
    new_post.img = File(new_path)
    new_post.author = img_post.author
    new_post.is_public = img_post.is_public
    new_post.parent = img_post
    new_post.description = img_post.description
    for tag in img_post.tags.all():
        new_post.tags.add(tag)
    new_post.save()

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
        
        rotate = int(form['rotate'].value())
        if rotate != 0 and rotate != 360:
            create_img(img_post, 'rotate', angle=rotate)
        
        return render(request, 'success.html')

    return render(request, 'process.html', {'img': img_post, 'form': ProcessForm()})
        
def filtershow(request):
    return render(request, 'filter.html')

def home(request):
    return render(request, 'home.html')
