from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MyUser(User):
    nickname = models.CharField(max_length=20, blank=True)
    gender = models.BooleanField(default=True)
    followings = models.ManyToManyField('self', blank=True)
    blacklist = models.ManyToManyField('self', blank=True)