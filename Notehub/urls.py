from django.contrib import admin
from django.urls import path
from Notehub.views import *
from Notehub.views import upload,add_user_note

from django.conf.urls.static import static

appname = 'Notehub'
urlpatterns = [
    path("uploadPicture", upload, name='upload'),
    path('showPicture', show, name='show'),
    path('login', login, name='login'),
    path('draw', draw)
    ]
