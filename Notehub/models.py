from django.db import models
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.db.models import F, Q


# Create your models here.
class Note(models.Model):
    id = models.AutoField(primary_key=True)
    # 定义varchar字段
    img_name = models.CharField(max_length=32)
    img_path = models.CharField(max_length=32)
    data = models.ImageField(upload_to='static/notedata')
    upload_time = models.DateTimeField(auto_now_add=True)
    uploader= models.CharField(max_length=32)


class User(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    username = models.CharField(max_length=32, null=False, primary_key=True)
    password = models.CharField(max_length=256, null=False)
    sex = models.CharField(max_length=8, choices=gender, null=True)
    # phone = models.CharField(max_length=16, null=True)
    email = models.EmailField(unique=True)
    isAdmin = models.CharField(max_length=1, default=0)


class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=32, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256,
                                widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
