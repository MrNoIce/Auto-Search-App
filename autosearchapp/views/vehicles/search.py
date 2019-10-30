from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse


import requests


def search(request):
    r = requests.get('http://localhost:5002/listings', params=request.GET)
    searched_vehicles = r.json()
    template = 'vehicles/searchresults.html'
    context = {
        'searched_vehicles': searched_vehicles
    }
    return render(request, template, context)


def index(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles' : ['Admin','User']
    }

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
