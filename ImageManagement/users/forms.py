from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from .models import MyUser
from django import forms

class LoginForm(AuthenticationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']

class SignupForm(UserCreationForm):
    email = forms.EmailField(label='电子邮箱')
    nickname = forms.CharField(label='昵称')
    gender = forms.ChoiceField(label='性别', choices=[(0, '男'), (1, '女')])
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
    email = forms.EmailField(label='电子邮箱')
    nickname = forms.CharField(label='新昵称')
    gender = forms.ChoiceField(label='性别', choices=[(0, '男'), (1, '女')])

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
    username = forms.CharField(label = '请输入用户名称')