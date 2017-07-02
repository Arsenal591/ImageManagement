from users.models import MyUser
from images.models import ImagePost
from django.db import models
from django.utils import timezone

TIMELINE_TYPE = [('like', 'like'), ('collect', 'collect'), ('comment', 'comment')]
class Timeline(models.Model):
    type = models.CharField(max_length=10, choices=TIMELINE_TYPE)
    sender_id = models.ForeignKey(MyUser, related_name='sends')
    image_id = models.ForeignKey(ImagePost)
    receiver_id = models.ForeignKey(MyUser, related_name='receives')
    occur_time = models.TimeField(default=timezone.now)
    comment_text = models.CharField(default='', max_length=140, blank=True)