from users.models import MyUser
from .models import Timeline

# user上传了图片image
def create_post_timeline(user, image):
    new_timeline = Timeline.objects.create(type='post', sender_id=user, image_id=image)
    new_timeline.original = new_timeline
    new_timeline.save()

# user给timeline点了赞
def create_like_timeline(user, timeline):
    # 谁被点了赞
    receiver = timeline.original.sender_id if timeline.original.type == 'post'else timeline.original.receiver_id
    new_timeline = Timeline.objects.create(type='like', 
                                           original=timeline.original, 
                                           sender_id=user, 
                                           image_id=timeline.original.image_id, 
                                           receiver_id=receiver)
    new_timeline.save()

# user收藏了timeline上的图片
def create_collect_timeline(user, timeline):
    receiver = timeline.original.sender_id if timeline.original.type == 'post'else timeline.original.receiver_id
    new_timeline = Timeline.objects.create(type='collect', 
                                           original=timeline.original, 
                                           sender_id=user, 
                                           image_id=timeline.original.image_id, 
                                           receiver_id=receiver)
    new_timeline.save()

# user给timeline上的图片评论了comment
def create_comment_timeline(user, timeline, comment):
    receiver = timeline.original.sender_id if timeline.original.type == 'post'else timeline.original.receiver_id
    new_timeline = Timeline.objects.create(type='comment', 
                                           original=timeline.original, 
                                           sender_id=user, 
                                           image_id=timeline.original.image_id, 
                                           receiver_id=receiver,
                                           comment_text=comment)
    new_timeline.save()