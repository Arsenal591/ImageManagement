from .timeline_generator import *
from images.models import ImagePost
from users.models import MyUser

# ͼƬimage�����˼�����
def get_image_like_num(image):
    likes = image.timeline_set.filter(type='like')
    return likes.count()

# ͼƬimage���ղ��˼���
def get_image_collect_num(image):
    collects = image.timeline_set.filter(type='collect')
    return collects.count()

# ͼƬimage�������˼���
def get_image_comment_num(image):
    comments = image.timeline_set.filter(type='comment')
    return comments.count()

# �ҵ���ͼƬ���޵������û�
# ����ֵ����MyUser��Ķ�����ɵ��б�
def get_image_liked(image):
    # �ҵ����ͼƬ�йصĵ���ʱ���ߣ�����ʱ������
    timelines = image.timeline_set.filter(type='like').order_by('occur_time').reverse()
    # �ҵ���Щʱ���ߵķ����ߣ���������
    users_id = timelines.values_list('sender_id', flat=True)
    users = MyUser.objects.filter(id__in=users_id)
    return users

# �ҵ��ղظ�ͼƬ�������û�
# ����ֵ����MyUser��Ķ�����ɵ��б�
def get_image_collected(image):
    timelines = image.timeline_set.filter(type='collect').order_by('occur_time').reverse()
    users_id = timelines.values_list('sender_id', flat=True)
    users = MyUser.objects.filter(id__in=users_id)
    return users

# �ҵ����۸���Ƭ�������û�����Ӧ�����ۡ��ͷ���ʱ��
# ����ֵ��ֱ�ӷ�����ص�timeline
def get_image_commented(image):
    timelines = image.timeline_set.filter(type='comment').order_by('occur_time').reverse()
    return timelines

# �ҵ�user�ղص�ͼƬ����
# ����ֵ����ͼƬ��ɵ��б�
def get_image_collection(user):
    timelines = user.sends.filter(type='collect').order_by('occur_time').reverse()
    images_id = timelines.values_list('image_id', flat=True)
    images = ImagePost.objects.filter(id__in=images_id)
    return images