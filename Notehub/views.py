import os
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from hackathon2022 import settings
import hashlib
from .models import Note, User, UserForm, RegisterForm

def add_user_note(request):
    all_images = Note.objects.all()
    return render(request, 'upload.html', locals())

def draw(request):
    error = ''
    if request.method == 'POST':
        img = request.FILES['img']
        pic_name = img.name
        if pic_name.split('.')[-1] == 'mp4':
            error = '暂不支持上传此格式图片！！！'
        else:
            Note.objects.create(img_name=pic_name, img_path="static/notedata/", data=img, uploader="test")
            return redirect(show)
    return render(request, 'draw.html', locals())

def upload(request):
    error = ''
    if request.method == 'POST':
        img = request.FILES['img']
        pic_name = img.name
        if pic_name.split('.')[-1] == 'mp4':
            error = '暂不支持上传此格式图片！！！'
        else:
            Note.objects.create(img_name=pic_name, img_path="static/notedata/", data=img,uploader="sb")
            return redirect(show)
    return render(request, 'upload.html', locals())


def show(request):
    all_images = Note.objects.all()
    # for i in all_images:
    #     print(i.data)
    return render(request, 'show.html', locals())


def encrypt(s, salt='mysite'):  # 密码加密
    h = hashlib.sha1()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()


def login(request):
    # if request.session.get('is_login', None):  # 不重复登录
    #     return redirect('/app01/index')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == encrypt(password):
                    request.session['is_login'] = True
                    request.session['user_name'] = user.username
                    if user.isAdmin != "0":
                        request.session['is_admin'] = True
                    else:
                        request.session['is_admin'] = False
                    return show(request=request)
                else:
                    message = "密码错误，请重新输入！"
            except:
                message = "用户不存在，请检查输入信息或注册账号！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    # if request.session.get('is_login', None):  # 登录状态不允许注册
    #     return redirect("/app01/index")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查所填内容！验证码可能有误"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '该用户名已被注册，想想其他的吧！'
                    return render(request, 'register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱已被注册，试试其他邮箱！'
                    return render(request, 'register.html', locals())

                new_user = User.objects.create(username=username, password=encrypt(password1), email=email,
                                                      sex=sex)
                return redirect('/app01/login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, "register.html", locals())

def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/app01/index")
    request.session.flush()  # 清空session中的内容
    return redirect("/app01/index")