from django.contrib import admin
from .models import ImagePost, ImageTag
from django.contrib.auth.models import User

admin.site.register(ImageTag)
admin.site.register(ImagePost)
#admin.site.register(ImageComment)
