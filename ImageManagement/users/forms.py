from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
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
    def save(self, commit=True):
        new_user = super().save(commit=False)
        new_user.email = self.cleaned_data['email']
        new_user.nickname = self.cleaned_data['nickname']
        new_user.gender = self.cleaned_data['gender']
        if commit:
            new_user.save()
        return new_user

class UpdateInfoForm(forms.ModelForm):
    old_password = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}))
    new_password = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}))
    new_password_2 = forms.CharField(widget=forms.TextInput(attrs={'type':'password'}))
    email = forms.EmailField()
    nickname = forms.CharField()
    gender = forms.BooleanField(required=False)

    class Meta:
        pass
