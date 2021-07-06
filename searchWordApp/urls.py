from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from . import views as myview
from rest_framework import routers
from django.http import HttpResponse




urlpatterns = [
    path('', myview.index,name='index'),
    path('searchWord', myview.searchWord, name='searchWord'),
]