from .timeline_generator import *
from images.models import ImagePost
from users.models import MyUser

# 图片image被点了几次赞
def get_image_like_num(image):
    likes = image.timeline_set.filter(type='like')
    return likes.count()

# 图片image被收藏了几次
def get_image_collect_num(image):
    collects = image.timeline_set.filter(type='collect')
    return collects.count()

# 图片image被评论了几次
def get_image_comment_num(image):
    comments = image.timeline_set.filter(type='comment')
    return comments.count()

# 找到给图片点赞的所有用户
# 返回值：由MyUser类的对象组成的列表
def get_image_liked(image):
    # 找到与该图片有关的点赞时间线，并按时间排序
    timelines = image.timeline_set.filter(type='like').order_by('occur_time')
    # 找到这些时间线的发出者，即点赞者
    users = timelines.values_list('sender_id', flat=True)
    return users

# 找到收藏该图片的所有用户
# 返回值：由MyUser类的对象组成的列表
def get_image_collected(image):
    timelines = image.timeline_set.filter(type='collect').order_by('occur_time')
    users = timelines.values_list('sender_id', flat=True)
    return users

# 找到评论该照片的所有用户、对应的评论、和发生时间
# 返回值：由字典组成的列表，每个字典都有三个字段，对应上面的三个元素
def get_image_commented(image):
    timelines = image.timeline_set.filter(type='comment').order_by('occur_time')
    result = timelines.values_list('sender_id', 'comment_text', 'occur_time')
    return result

# 找到user收藏的图片集合
# 返回值：由图片组成的列表
def get_image_collection(user):
    timelines = user.sends.filter(type='collect').order_by('occur_name')
    return timelines.values_list('image_id', flat=True)