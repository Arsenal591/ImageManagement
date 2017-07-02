from .timeline_generator import *
from images.models import ImagePost
from users.models import MyUser

def get_image_like_num(image):
    likes = image.timeline_set.filter(type='like')
    return likes.count()

def get_image_collect_num(image):
    collects = image.timeline_set.filter(type='collect')
    return collects.count()

def get_image_comment_num(image):
    comments = image.timeline_set.filter(type='comment')
    return comments.count()

def get_image_liked(image):
    timelines = Timeline.objects.filter(image_id=image, type='like').order_by('occur_time')
    users = timelines.values_list('sender_id', flat=True)
    return users

def get_image_collected(image):
    timelines = Timeline.objects.filter(image_id=image, type='collect').order_by('occur_time')
    users = timelines.values_list('sender_id', flat=True)
    return users

def get_image_commented(image):
    timelines = Timeline.objects.filter(image_id=image, type='comment').order_by('occur_time')
    result = timelines.values_list('sender_id', 'comment_text')
    return result

def get_image_collection(user):
    timelines = Timeline.objects.filter(sender_id=user, type='collect').order_by('occur_time')
    return timelines.values_list('image_id', flat=True)