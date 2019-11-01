from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from secrets import API_KEY
import json
import os




import requests

@login_required
def search(request):

    year = request.GET['year']
    make = request.GET['make']
    model = request.GET['model']

    url = "http://api.marketcheck.com/v1/search"

    querystring = {"api_key":API_KEY,"year":year,"make":make,"model":model,"latitude":"36.16","longitude":"-86.78","radius":"50","car_type":"used","start":"0","rows":"50"}

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