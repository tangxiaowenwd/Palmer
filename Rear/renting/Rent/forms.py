# Author:Palmer
# _*_ coding:utf-8 _*_
# Time:2020/10/19 21:52
from django import forms
#from captcha import CaptchaField

Sex = [
    ("0", "男"),
    ("1", "女")
]


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RentForm(forms.Form):
    user = forms.CharField(label="昵称", max_length=128)
    phone = forms.CharField(label="手机号码", max_length=11)
    sex = forms.ChoiceField(label="性别", choices=Sex)


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)

