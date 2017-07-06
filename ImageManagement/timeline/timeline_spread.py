from users.models import MyUser
from .models import Timeline

def create_post_timeline(user, image):
    new_timeline = Timeline.objects.create(type='post', sender_id=user, image_id=image)
    new_timeline.original = new_timeline
    new_timeline.save()
    return new_timeline

def create_like_timeline(user, image):
    receiver = image.author
    #receiver = timeline.original.sender_id if timeline.original.type == 'post'else timeline.original.receiver_id
    new_timeline = Timeline.objects.create(type='like', 
                                           sender_id=user, 
                                           image_id=image, 
                                           receiver_id=receiver)
    new_timeline.save()
    return new_timeline

def create_collect_timeline(user, image):
    receiver = image.author
    #receiver = timeline.original.sender_id if timeline.original.type == 'post'else timeline.original.receiver_id
    new_timeline = Timeline.objects.create(type='collect',  
                                           sender_id=user, 
                                           image_id=image, 
                                           receiver_id=receiver)
    new_timeline.save()
    return new_timeline

def create_comment_timeline(user, image, comment):
    receiver = image.author
    #receiver = timeline.original.sender_id if timeline.original.type == 'post'else timeline.original.receiver_id
    new_timeline = Timeline.objects.create(type='comment', 
                                           sender_id=user, 
                                           image_id=image,
                                           receiver_id=receiver,
                                           comment_text=comment)
    new_timeline.save()
    return new_timeline