from django.db import models
from django.utils import timezone

class ImageTag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class ImagePost(models.Model):
    author = models.ForeignKey('auth.User')
    tag = models.ForeignKey(ImageTag, blank=True)
    path = models.CharField(max_length=100)
    if_public = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
    heat = models.IntegerField(default=0)

class ImageComment(models.Model):
    image = models.ForeignKey(ImagePost, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
# Create your models here.
