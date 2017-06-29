from django.db import models
from django.utils import timezone

class ImageTag(models.Model):
    name = models.CharField(max_length=20)
    images = models.ManyToManyField('images.ImagePost', blank=True)

    def __str__(self):
        return self.name

class ImagePost(models.Model):
    author = models.ForeignKey('auth.User')
    tags = models.ManyToManyField(ImageTag, blank=True)
    path = models.CharField(max_length=100)
    is_public = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    heat = models.IntegerField(default=0)
    
    def __str__(self):
        return self.path

class ImageComment(models.Model):
    image = models.ForeignKey(ImagePost, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    author = models.ForeignKey('auth.User')
    
    def __str__(self):
        return content

