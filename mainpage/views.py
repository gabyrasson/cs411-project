from django.shortcuts import render
from django.http import HttpResponse
import requests
from .forms import SearchForm


def index(request):
    return HttpResponse("CS411 Project")


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
    querystring = {"auth_token": "JteLYfPY2XpyCb8ZkxBr", "type": typetake}
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "1993f52c-ade4-461a-8481-0ea4ac8176f9"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    re_response = response.json()
    return render(request, 'showprotoresult.html', {'response_dict': re_response})


def showreports(request, country, distype):
    url = "https://api.reliefweb.int/v1/reports"

    querystring = {
        "query[value]": country.lower() + " AND " + distype.lower() + 's' + " OR " + distype.lower(),
        "sort[]": "date:desc", "limit": "20", "": ""}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response.text)
    re_response = response.json()
    return render(request, 'showreports.html', {'response': re_response})


def showjobs(request, country):
    url = "https://api.reliefweb.int/v1/jobs"

    querystring = {"query[fields][]": "country", "query[value]": country, "sort[]": "date:desc", "limit": "300", "": ""}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }

    response_jobs = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response_jobs.text)

    re_response1 = response_jobs.json()

    url = "https://api.reliefweb.int/v1/training"

    querystring = {"query[fields][]": "theme.name", "query[value]": "Disaster Management", "sort[]": "date:desc",
                   "limit": "300", "": ""}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }

    response_training = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response_training.text)

    re_response2 = response_training.json()

    return render(request, 'showjobs.html', {'response1': re_response1, 'response2': re_response2})
