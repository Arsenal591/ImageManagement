from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from .models import MyUser
from django import forms
class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    nickname = forms.CharField()
    gender = forms.BooleanField()
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'nickname', 'gender']