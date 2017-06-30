from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import ImageTag, ImageComment, ImagePost
from django.contrib.auth.models import User
from django.utils import timezone
import time
import random
import os
from scipy import misc
from django.http import HttpResponse

def index(request):
    imgs = ImagePost.objects.order_by('-created_at')
    pub_imgs = [img for img in imgs if img.is_public]
    return render(request, 'index.html', {'imgs': pub_imgs})

def upload(request):
    return render(request, 'upload.html')

def upload_img(request):
    if request.method == 'POST':
        img = request.FILES['image']
        if img:
            img_file = misc.imread(img)
            img_suffix = str(img).split('.')[-1]
            series_num = str(time.time()).replace('.', '') + str(random.randint(0, 1000))
            save_path = '/static/images/'+series_num+'.'+img_suffix
            misc.imsave(os.getcwd()+'/images'+save_path, img_file)
            po = ImagePost()
            po.path = save_path
            po.created_at = timezone.now()
            po.save()
            return render(request, 'success.html')
        return render(requese, 'fail.html')



# Create your views here.
