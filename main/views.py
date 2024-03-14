from django.shortcuts import render
from django.http import *
from django.views.generic.base import TemplateView
import getToken
import json

# Create your views here.

#displaying the api requests
def displayAPI(request):
    token = getToken.get_token()
    response  = getToken.getArtist(token)
    response_str = response["name"]
    response_img= response["images"][2]["url"]
    return render(request, 'show.html', {'image' : response_img, 'data' : response_str})

def newReleases(request):
    token = getToken.get_token()
    newRAr, newRAN, newRURL = getToken.newReleases(token)
    return render(request, 'show.html', {'newReleaseArtist': newRAr, 'newReleaseAlbum': newRAN, 'newReleaseURL': newRURL})

