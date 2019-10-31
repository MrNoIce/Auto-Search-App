from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from secrets import API_KEY
import json
import os




import requests


def search(request):
    url = "http://api.marketcheck.com/v1/search"

    querystring = {"api_key":{API_KEY},"year":"2014","make":"ford","latitude":"34.05","longitude":"-118.24","radius":"100","car_type":"used","start":"0","rows":"50","seller_type":"dealer"}

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