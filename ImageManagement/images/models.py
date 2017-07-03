from django.db import models
from django.utils import timezone

class ImageTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

#class ImageHeat(models.Model):
#    author = models.ForeignKey(auth.User, null=True)
#    image = models.ForeignKey('ImagePost')
#
#    def __str__(self):
#        return "%s_%s" % (author.__str__, image.__str__)

class ImagePost(models.Model):
    # basic info
    author = models.ForeignKey('auth.User', null=True)
    tags = models.ManyToManyField(ImageTag)
    is_public = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    like_num = models.IntegerField(default=0)
    collect_num = models.IntegerField(default=0)
    description = models.CharField(max_length=140, null=True)
    img = models.ImageField(null=True)
    # edit from some picture?
    parent = models.ForeignKey('self', null=True)

    def __str__(self):
        return str(self.id)

#class ImageComment(models.Model):
#    image = models.ForeignKey(ImagePost, on_delete=models.CASCADE)
#    content = models.CharField(max_length=140)
#    author = models.ForeignKey('auth.User')
#    previous = models.ForeignKey('ImageComment', null=True)
#    pub_time = models.DateTimeField(default=timezone.now)
#    
#    def __str__(self):
#        return content

