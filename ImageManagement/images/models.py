from django.db import models
from django.utils import timezone


# explanation:
# originally, one TagNo maps to one ImageTag
# but this mapping is too detailed
# for example, one TagNo maybe 'salmon', while another TagNo is 'shark'
# for simplity, we all link the two TagNo to ImageTag 'fish'

class ImageTag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class TagNo(models.Model):
    no = models.CharField(max_length=32)
    tag = models.ForeignKey(ImageTag)

    def __str__(self):
        return self.no

class ImagePost(models.Model):

    # basic info
    author = models.ForeignKey('auth.User', null=True)
    tags = models.ManyToManyField(ImageTag)
    is_public = models.BooleanField(default=True, verbose_name='public')
    created_at = models.DateTimeField(default=timezone.now)
    like_num = models.IntegerField(default=0)
    collect_num = models.IntegerField(default=0)
    description = models.CharField(max_length=140, null=True)
    img = models.ImageField(null=True, verbose_name='image')
    # edit from some picture?
    parent = models.ForeignKey('self', null=True)

    def __str__(self):
        return str(self.id)

