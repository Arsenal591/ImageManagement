from ..users.models import MyUser
from ..images.models import ImagePost
from django.db import models
from django.utils import timezone

class TimelineComment(models.Model):
    sender_id = models.ForeignKey(MyUser)
    timeline_id = models.ForeignKey('Timeline')
    receiver_id = models.ForeignKey(MyUser)
    occur_time = models.TimeField(default=timezone.now)
# Create your models here.
class Timeline(models.Model):
    user_id = models.ForeignKey(MyUser)
    occur_time = models.DateTimeField(default=timezone.now)
    image_ids = models.ManyToManyField(ImagePost, blank=True)
    like_num = models.IntegerField(default=0)
    collected_num = models.IntegerField(default=0)
    comments_num = models.IntegerField(default=0)
    comments_id = models.ManyToManyField(TimelineComment, blank=True)