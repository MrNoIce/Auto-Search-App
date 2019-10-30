from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
import json



import requests

# api_key='JKI2W87ezyF2ZHkM1T43LAhb72ZFZgas'
# host='marketcheck-prod.apigee.net'

# def search(request):
#     api_key='JKI2W87ezyF2ZHkM1T43LAhb72ZFZgas'
#     host='marketcheck-prod.apigee.net'
#     url = f'http://api.marketcheck.com/search?api_key={api_key}&year=2014&make=ford&latitude=34.05&longitude=-118.24&radius=100&car_type=used&start=0&rows=50&seller_type=dealer'
#     headers = {'Host': 'marketcheck-prod.apigee.net', 'Content-Type': "application/json"}
#     PARAMS = {'api_key': 'JKI2W87ezyF2ZHkM1T43LAhb72ZFZgas'}
#     r = requests.get(url, headers=headers, params=PARAMS)
#     searched_vehicles = r.json()
#     template = 'vehicles/searchresults.html'
#     context = {
#         'searched_vehicles': searched_vehicles
#     }
#     return render(request, template, context)

def search(request):
    url = "http://api.marketcheck.com/v1/search"

    querystring = {"api_key":"JKI2W87ezyF2ZHkM1T43LAhb72ZFZgas","year":"2014","make":"ford","latitude":"34.05","longitude":"-118.24","radius":"100","car_type":"used","start":"0","rows":"50","seller_type":"dealer"}

    headers = {
        'Host': "marketcheck-prod.apigee.net",
        'Content-Type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    searched_vehicles = response.json()
    template = 'vehicles/searchresults.html'
    context = {
        'searched_vehicles': searched_vehicles
    }

    return render(request, template, context)


    print(response.json)

# def index(request):
#     responseData = {
#         'id': 4,
#         'name': 'Test Response',
#         'roles' : ['Admin','User']
#     }


def search1(request):
    # api-endpoint
    URL = "http://{{host}}/search?api_key={{api_key}}&year=2014&make=ford&model=f150&latitude=34.05&longitude=-118.24&radius=10000&car_type=used&start=0&rows=10"

    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'year':year}

    # sending get request and saving the response as response object
    r = requests.get(url = URL, params = PARAMS)

    # extracting data in json format
    data = r.json()
    template = 'vehicles/searchresults.html'
    context = {
        'searched_vehicles': searched_vehicles
    }
    return render(request, template, context)


# r = requests.get('http://localhost:5002/listings', params=request.GET)
#     if media.photo_links in r != null:
#         searched_vehicles = r.json()
#         template = 'vehicles/searchresults.html'
#         context = {
#             'searched_vehicles': searched_vehicles
#         }
# , HttpResponse(searched_vehicles, content_type='application/json')

# def search(request):

#     if request.method == "GET":
#         # url = form.cleaned_data['url']
#         r = requests.get('http://localhost:5002/listings')
#         json = r.json()
#         print(json)
#     return render(request)
