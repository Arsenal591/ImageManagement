from django import forms
from .models import ImagePost, ImageTag

class UploadForm(forms.ModelForm):
    tags = forms.CharField(max_length=512)
    class Meta:
        model = ImagePost
        fields = ('description','is_public', 'img')

class ProcessForm(forms.Form):
    gray = forms.BooleanField(required=False, label='generate a gray copy')
    to_blur = forms.BooleanField(required=False, label='generate a blur copy')
    blur = forms.FloatField(min_value=0,  max_value=1, required=False, disabled=True, label='blur level(0~1)')
    binaryzation = forms.BooleanField(required=False, label='generate a binary copy')
    to_rescale = forms.BooleanField(required=False, label='generate a rescaled copy')
    rescale = forms.FloatField(required=False, min_value=0.1, max_value=5, disabled=True, label='ratio(0.001~5)')
    to_rotate = forms.BooleanField(required=False, label='generate a rotated copy')
    rotate = forms.IntegerField(min_value=0, max_value=360, required=False, disabled=True, label='rotate angle(anticlockwise, 0~360)')

class BatchUploadForm(forms.Form):
    description = forms.CharField(max_length=140, required=False)
    is_public = forms.BooleanField(required=False, label='Public')
    img_batch = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}), label='Images')
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
    user_filter = forms.ChoiceField(choices=user_choices, label='Author of the images')
    username = forms.CharField(max_length=128, required=False, label='Specified username(not required)')
    auth_filter = forms.ChoiceField(choices=auth_choices, label='Authority settings')
    between_date = forms.BooleanField(required=False, label='During date range')
    date_start = forms.DateField(required=False, widget=forms.SelectDateWidget, disabled=True, label='')
    date_end = forms.DateField(required=False, widget=forms.SelectDateWidget, disabled=True, label='')
    tags = forms.CharField(max_length=512, required=False)

class DetailForm(forms.Form):
    like = forms.BooleanField(required=False)
    collect = forms.BooleanField(required=False)

class ImgSrchForm(forms.Form):
    img = forms.ImageField(required=True, label='source image')


