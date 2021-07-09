from django.http import HttpResponse,JsonResponse
from django.shortcuts import render,redirect
from datetime import datetime
from django.views.generic import View
from django.contrib.auth.models import User, Group, auth
from rest_framework import viewsets
from rest_framework import permissions
from django.http import HttpResponse
import urllib, json


def index(request):
    return render(request, "index.html", {})


def searchWord(request):
    word_id = request.POST["wordTitle"];
    language = 'en_US'
    url = 'https://api.dictionaryapi.dev/api/v2/entries/'  + language + '/'  + word_id.lower()
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    print(data)
    return render(request, "index.html", {"wordDetail": data[0]})
