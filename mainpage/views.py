from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import SearchForm


def index(request):
    return HttpResponse("CS411 Project Prototype")

def get_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            typins = form.cleaned_data['typein']
            # types: earthquakes, floods, cyclones, volcanoes
            return showprotoresult(request, typins)
    else:
        form = SearchForm()
    return render(request, 'searchbar.html', {'form': form})


def showprotoresult(request, typetake):
    url = "http://api.sigimera.org/v1/crises"
    querystring = {"auth_token": "...","type": typetake}
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    re_response = response.json()
    return render(request, 'showprotoresult.html', {'response_dict': re_response})
