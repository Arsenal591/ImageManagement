from django.db import models
from django.utils import timezone

class ImageTag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class ImagePost(models.Model):
    author = models.ForeignKey('auth.User')
    comment = models.CharField(max_length=140)
    tags = models.ManyToManyField(ImageTag, blank=True)
    path = models.CharField(max_length=100)
    original_path = models.CharField(max_length=100)
    if_original = models.BooleanField()
    if_public = models.BooleanField()
    created_at = models.DateTimeField(default=timezone.now)
# Create your models here.
