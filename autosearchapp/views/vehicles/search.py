from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from secrets import API_KEY
import json
import os


# this handles the request to my external api

import requests

@login_required
def search(request):

    year = request.GET['year']
    make = request.GET['make']
    model = request.GET['model']
    zip_code = request.GET['zip']
    max_price = request.GET['max_price']

    url = "http://api.marketcheck.com/v1/search"

    querystring = {"api_key":API_KEY,"seller_type":"private","year":year,"make":make,"model":model,"zip":zip_code,"radius":"200","car_type":"used","start":"0","rows":"50","price_range":max_price,}

    headers = {
        'Host': "marketcheck-prod.apigee.net",
        'Content-Type': "application/json"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response, 'response')
    searched_vehicles = response.json()
    template = 'home.html'
    context = {
        'searched_vehicles': searched_vehicles
    }

    return render(request, template, context)