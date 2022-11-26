import os
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse
from djangoProject import settings
from .models import Note

def test(request):
    return HttpResponse('hello')
# Create your views here.
# def add_note(request):
#     if request.method == 'GET':
#         class_Note =

# /uploal_action/


def add_user_note(request):
    return render(request, 'index.html')


def upload(request):
    error = ''
    if request.method == 'POST':
        img = request.FILES.get('img')
        pic_name = img.name
        if pic_name.split('.')[-1] == 'mp4':
            error = '暂不支持上传此格式图片！！！'
        else:
            Note.objects.create(id='1',img_name=pic_name, img_path=pic_name, data=img)
            return redirect('show')
    return render(request, 'index.html', locals())

def show(request):
    all_images = Note.objects.all()
    # for i in all_images:
    #     print(i.img)
    return render(request, 'show.html', locals())