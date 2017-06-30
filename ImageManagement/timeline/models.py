from users.models import MyUser
from images.models import ImagePost
from django.db import models
from django.utils import timezone

class BasicTimeline(models.Model):
    sender_id = models.ForeignKey(MyUser, related_name='sender')
    image_id = models.ForeignKey(ImagePost)
    receiver_id = models.ForeignKey(MyUser, related_name='receiver')
    occur_time = models.TimeField(default=timezone.now)

class Like(BasicTimeline):
    pass

class Collect(BasicTimeline):
    pass

class Comment(BasicTimeline):
    text = models.CharField(default='', max_length=140)
