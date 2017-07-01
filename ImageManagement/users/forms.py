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
    gender = forms.BooleanField(required=False)
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'nickname', 'gender']
    def save():
        pass
        #new_user = super(U)

class ChangeInfoForm():
    pass