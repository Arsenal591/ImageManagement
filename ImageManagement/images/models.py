from django.db import models
from django.utils import timezone

class ImageTag(models.Model):
    name = models.CharField(max_length=20)
    images = models.ManyToManyField('ImagePost')

    def __str__(self):
        return self.name

class ImagePost(models.Model):
    # basic info
    author = models.ForeignKey('auth.User', null=True)
    tags = models.ManyToManyField(ImageTag)
    path = models.CharField(max_length=128)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    heat = models.IntegerField(default=0)
    description = models.CharField(max_length=140, null=True)
    # relationships
    siblings = models.ManyToManyField('ImagePost')
    comments = models.ManyToManyField('ImageComment')

    def __str__(self):
        return self.path

class ImageComment(models.Model):
    image = models.ForeignKey(ImagePost, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    author = models.ForeignKey('auth.User')
    previous = models.ForeignKey('ImageComment', null=True)
    pub_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return content

