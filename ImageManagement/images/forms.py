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

class FilterForm(forms.Form):
    user_choices = (
        ('All', 'All'),
        ('Mine', 'Mine'),
        ('Specified user', 'Specified user')
    )
    auth_choices = (
        ('All', 'All'),
        ('Public', 'Public'),
        ('Private', 'Private')
    )
    
    user_filter = forms.ChoiceField(choices=user_choices)
    username = forms.CharField(max_length=128, required=False)
    auth_filter = forms.ChoiceField(choices=auth_choices)
    between_date = forms.BooleanField(required=False)
    date_start = forms.DateField(required=False, widget=forms.SelectDateWidget)
    date_end = forms.DateField(required=False, widget=forms.SelectDateWidget)
    tags = forms.CharField(max_length=512, required=False)

class DetailForm(forms.Form):
    like = forms.BooleanField(required=False)
    collect = forms.BooleanField(required=False)

class ImgSrchForm(forms.Form):
    img = forms.ImageField(required=True)


