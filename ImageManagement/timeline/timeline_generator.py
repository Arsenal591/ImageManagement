from .models import Timeline
from users.models import MyUser

def select_object_timeline_by_user(request_user, target_user):
    flag1 = (target_user in request_user.blacklist.all()) 
    flag2 = (target_user in request_user.blacklist.all())

    if flag1 > 0 or flag2 > 0:
        print("blacked")
        return Timeline.objects.none()
    else:
        result = Timeline.objects.filter(sender_id=request_user, image_id__is_public=1)
        return result

def select_object_timeline_by_name(request_name, target_name):
    request_user = MyUser.objects.get(username=request_name)
    target_user = MyUser.objects.get(username=target_name)

    assert (request_user is not None) and (target_user is not None)

    return select_object_timeline_by_user(request_user, target_user)


def select_subject_timeline_by_user(user):
    followings = user.followings.all()
    timelines = Timeline.objects.none()

    for follow in followings:
        user_timeline = select_object_timeline_by_user(user, follow)
        timelines = timelines | user_timeline

    return timelines

def select_subject_timeline_by_name(request_name):
    request_user = MyUser.objects.get(username=request_name)

    assert request_user is not None

    return select_subject_timeline_by_user(request_user)

def timeline_generate(type, sender, image, receiver, comment):
    new_timeline = Timeline.objects.create(type=type, sender_id=sender, 
                                           image_id=image, receiver_id=receiver, comment_text=comment)
    new_timeline.save()