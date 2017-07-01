from django import forms
from .models import ImagePost, ImageTag

class EditForm(forms.ModelForm):
    description = forms.CharField(label='description', max_length=140)
    tags = forms.MultipleChoiceField(ImageTag.objects.all())
    is_pulic = forms.BooleanField()