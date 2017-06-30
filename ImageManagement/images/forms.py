from django import forms
from .models import ImagePost, ImageComment, ImageTag



class UploadImgForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ('is_public', 'description')


