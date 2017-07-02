from django import forms
from .models import ImagePost, ImageTag

class UploadForm(forms.ModelForm):
    tags = forms.CharField(max_length=512)
    class Meta:
        model = ImagePost
        fields = ('description','is_public', 'img')

class ProcessForm(forms.Form):
    gray = forms.BooleanField(required=False)
    blur = forms.FloatField(min_value=0,  max_value=1, required=False)
    binaryzation = forms.BooleanField(required=False)
    rescale = forms.FloatField(min_value=0.001, max_value=5)
    rotate = forms.IntegerField(min_value=0, max_value=360, required=False)

class BatchUploadForm(forms.Form):
    is_public = forms.BooleanField(required=False)
    description = forms.CharField(max_length=140, required=False)
    img_batch = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    tags = forms.CharField(max_length=512)



