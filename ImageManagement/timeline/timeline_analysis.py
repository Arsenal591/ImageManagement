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
    timelines = image.timeline_set.filter(type='like').order_by('occur_time')
    # �ҵ���Щʱ���ߵķ����ߣ���������
    users = timelines.values_list('sender_id', flat=True)
    return users

# �ҵ��ղظ�ͼƬ�������û�
# ����ֵ����MyUser��Ķ�����ɵ��б�
def get_image_collected(image):
    timelines = image.timeline_set.filter(type='collect').order_by('occur_time')
    users = timelines.values_list('sender_id', flat=True)
    return users

# �ҵ����۸���Ƭ�������û�����Ӧ�����ۡ��ͷ���ʱ��
# ����ֵ�����ֵ���ɵ��б�ÿ���ֵ䶼�������ֶΣ���Ӧ���������Ԫ��
def get_image_commented(image):
    timelines = image.timeline_set.filter(type='comment').order_by('occur_time')
    result = timelines.values_list('sender_id', 'comment_text', 'occur_time')
    return result

# �ҵ�user�ղص�ͼƬ����
# ����ֵ����ͼƬ��ɵ��б�
def get_image_collection(user):
    timelines = user.sends.filter(type='collect').order_by('occur_name')
    return timelines.values_list('image_id', flat=True)