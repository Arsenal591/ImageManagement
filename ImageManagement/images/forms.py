from django import forms
from .models import ImagePost, ImageTag

class UploadForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ('description','tags', 'is_public', 'img')

class ProcessForm(forms.Form):
    gray = forms.BooleanField(required=False)
    blur = forms.FloatField(min_value=0,  max_value=1, required=False)
    binaryzation = forms.BooleanField(required=False)
    rescale = forms.FloatField(min_value=0.001, max_value=5)
    
