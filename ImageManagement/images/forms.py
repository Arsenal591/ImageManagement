from django import forms
from .models import ImagePost, ImageTag

class UploadForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ('description','tags', 'is_public', 'img')

class EditForm(forms.ModelForm):
    description = forms.CharField(label='description', max_length=140)
    tags = forms.MultipleChoiceField(ImageTag.objects.all())
    is_pulic = forms.BooleanField()
