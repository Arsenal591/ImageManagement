from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(ImageTag)
admin.site.register(ImagePost)
admin.site.register(TagNo)
#admin.site.register(ImageComment)
