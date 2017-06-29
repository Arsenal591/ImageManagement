from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import ImageTag, ImageComment, ImagePost

def index(request):
    imgs = ImagePost.objects.order_by('-created_at')
    return render(request, 'index.html', {'imgs': imgs})




# Create your views here.
