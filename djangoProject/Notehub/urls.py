from django.contrib import admin
from django.urls import path

from Notehub.views import test, add_user_note,upload
appname = 'Notehub'
urlpatterns = [
    path('test1', upload, name='index')
    ]