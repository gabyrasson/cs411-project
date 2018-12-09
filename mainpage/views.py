from django.shortcuts import render
from django.http import HttpResponse
import requests
from requests.auth import HTTPBasicAuth
from .forms import SearchForm

from django.http import *


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
        'Postman-Token': "a37ddf5f-8cd7-4628-9224-8d79c10c402d"
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
        'Postman-Token': "8a16eed8-8cb6-412e-9655-ec47b87da3a9"
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
        'Postman-Token': "18898101-4b61-4f5d-830f-c9481fc763e2"
    }

    response_training = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    print(response_training.text)

    re_response2 = response_training.json()

    return render(request, 'showjobs.html', {'response1': re_response1, 'response2': re_response2})


def handjob(request, jobid):
    url = "https://api.reliefweb.int/v1/jobs/" + str(jobid)

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "f8d6d228-60a1-436d-9cc4-74913ff96184"
    }

    result = requests.request("GET", url, data=payload, headers=headers)

    print(result.text)
    resultjs = result.json()

    return render(request, 'handjob.html', {'result': resultjs})


def handtraing(request, traingid):
    url = "https://api.reliefweb.int/v1/training/" + str(traingid)

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "ae623c7d-b5b6-4fe2-8874-847c7476ab24"
    }

    result = requests.request("GET", url, data=payload, headers=headers)

    print(result.text)
    resultjs = result.json()
    return render(request, 'handtraing.html', {'result': resultjs})


def add_task(request):
    request_template = "https://api.toodledo.com/3/account/token.php"
    payload = {'grant_type': 'authorization_code', 'code': '16fa010f10c197f9b11907eb425152967677cd20'}
    request = request_template.format(**{'code': '16fa010f10c197f9b11907eb425152967677cd20', 'CLIENT_ID': 'cs411appuser', 'CLIENT_SECRET': 'api5c0d288c8dda3'})
    r = requests.post(request, params=payload, auth=HTTPBasicAuth('CLIENT_ID', 'CLIENT_SECRET'))
    re = r.json()
    print(re.text)
