import ast

from django.shortcuts import render
from django.http import HttpResponse
import requests


def index(request):
    return HttpResponse("CS411 Project Prototype")


def showprotoresult(request):
    url = "http://api.sigimera.org/v1/crises"
    querystring = {"auth_token": "..."}
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    re_response = response.json()
    return render(request, 'showprotoresult.html', {'response_dict': re_response})