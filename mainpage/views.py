import requests
from django.shortcuts import render
import requests_cache
from pip._vendor.distlib.compat import raw_input
from requests.auth import HTTPBasicAuth
from .forms import SearchForm
from django.http import *

requests_cache.install_cache('project_cache', backend='sqlite', expire_after=86400)


def index(request):
    return render(request, 'index.html')


def get_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            typins = form.cleaned_data['typein']
            print(typins=='floods')
            # types: earthquakes, floods, cyclones, volcanoes
            if (typins != 'earthquakes') and (typins != 'volcanoes') and (typins != 'floods') and (typins != 'cyclones') : return render(request, 'errorpage.html')
            return showprotoresult(request, typins)
    else:
        form = SearchForm()
    return render(request, 'searchbar.html', {'form': form})


def showprotoresult(request, typetake):
    url = "http://api.sigimera.org/v1/crises"
    querystring = {"auth_token": "...", "type": typetake}
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print("Used Cache: {0}".format(response.from_cache))
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


def handlereport(request, reportid):
    url = "https://api.reliefweb.int/v1/reports/" + str(reportid)

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }

    response = requests.request("GET", url, data=payload, headers=headers)

    print(response.text)
    result = response.json()

    return render(request, 'handlereport.html', {'result': result})


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


def handlejob(request, jobid):
    url = "https://api.reliefweb.int/v1/jobs/" + str(jobid)

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }

    result = requests.request("GET", url, data=payload, headers=headers)

    print(result.text)
    resultjs = result.json()

    return render(request, 'handlejob.html', {'result': resultjs})


def handtraing(request, traingid):
    url = "https://api.reliefweb.int/v1/training/" + str(traingid)

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }

    result = requests.request("GET", url, data=payload, headers=headers)

    print(result.text)
    resultjs = result.json()
    return render(request, 'handtraing.html', {'result': resultjs})


def get_token(request):
    client_auth = requests.auth.HTTPBasicAuth('cs411appuser', 'api5c0d288c8dda3')
    post_data = {
        'grant_type': 'authorization_code',
        'code': '...',
        'redirect_uri': 'https://www.toodledo.com/tasks',
        'state': 'In Development/Beta',
        'device': 'terminal'
    }

    response = requests.post('https://api.toodledo.com/3/account/token.php', auth=client_auth, data=post_data)
    full_token = response.json()
    return render(request, 'get_token.html', {'token': full_token})


def show_tasks(request):
    url = "http://api.toodledo.com/3/tasks/get.php"

    querystring = {"access_token": "...", "after": "1234567890",
                   "fields": "folder,star,priority"}

    payload = ""
    headers = {
        'cache-control': "no-cache",
        'Postman-Token': "..."
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    print(response.text)
    re = response.json()
    return render(request, 'showtasks.html', {'result': re})
