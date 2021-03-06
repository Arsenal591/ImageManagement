from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .models import MyUser
from django import forms

class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    nickname = forms.CharField(label='nickname')
    gender = forms.ChoiceField(label='gender', choices=[(False, 'male'), (True, 'female')])
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

class ChangeinfoForm(forms.Form):
    email = forms.EmailField(label='email')
    nickname = forms.CharField(label='nickname')
    gender = forms.ChoiceField(label='gender', choices=[(0, 'male'), (1, 'female')])

    def set_username(self, username):
        self.username = username

    def save(self, commit=True):
        tar_user = MyUser.objects.get(username=self.username)
        if not tar_user:
            raise forms.ValidationError('CANNOT FIND THIS USER')
        tar_user.email = self.cleaned_data['email']
        tar_user.nickname = self.cleaned_data['nickname']
        tar_user.gender = self.cleaned_data['gender']

        if commit:
            tar_user.save()
        return tar_user

class SearchForm(forms.Form):
    username = forms.CharField(label = 'Please enter the username')