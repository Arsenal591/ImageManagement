from .timeline_generator import *
from images.models import ImagePost
from users.models import MyUser

# return value: integer, the number of people likes this image.
def get_image_like_num(image):
    likes = image.timeline_set.filter(type='like')
    return likes.count()

def get_image_collect_num(image):
    collects = image.timeline_set.filter(type='collect')
    return collects.count()

def get_image_comment_num(image):
    comments = image.timeline_set.filter(type='comment')
    return comments.count()

# return value: list, each element of which is a MyUser object
def get_image_liked(image):
    timelines = image.timeline_set.filter(type='like').order_by('occur_time').reverse()
    users_id = timelines.values_list('sender_id', flat=True)
    users = MyUser.objects.filter(id__in=users_id)
    return users

def get_image_collected(image):
    timelines = image.timeline_set.filter(type='collect').order_by('occur_time').reverse()
    users_id = timelines.values_list('sender_id', flat=True)
    users = MyUser.objects.filter(id__in=users_id)
    return users

# return value: list, each element of which is a Timeline object
def get_image_commented(image):
    timelines = image.timeline_set.filter(type='comment').order_by('occur_time').reverse()
    return timelines

# return value: list, each element of which is a ImagePost object.
def get_image_collection(user):
    timelines = user.sends.filter(type='collect').order_by('occur_time').reverse()
    images_id = timelines.values_list('image_id', flat=True)
    images = ImagePost.objects.filter(id__in=images_id)
    return images