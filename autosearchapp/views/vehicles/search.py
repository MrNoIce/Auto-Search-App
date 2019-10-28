from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse


import requests


def search(request):
    headers = {}
    r = requests.get('http://localhost:5002/listings', params=request.GET)
    json = r.json()
    if r.status_code == 200:
        return HttpResponse('Yay, it worked')
    return JsonResponse(json)


def index(request):
    responseData = {
        'id': 4,
        'name': 'Test Response',
        'roles' : ['Admin','User']
    }




# def search(request):

#     if request.method == "GET":
#         # url = form.cleaned_data['url']
#         r = requests.get('http://localhost:5002/listings')
#         json = r.json()
#         print(json)
#     return render(request)
