from models import *
f = open('images/tags.list')
lines = f.readlines()
f.close()

for line in lines:
    no, name = line.split()
    tag_no = TagNo()
    tag_no.no = no
    try:
        tag_instance = ImageTag.objects.get(name=name)
        tag_no.tag = tag_instance
    except Exception as e:
        tag_instance = ImageTag()
        tag_instance.name = name
        tag_instance.save()
        tag_no.tag = tag_instance
    tag_no.save()



