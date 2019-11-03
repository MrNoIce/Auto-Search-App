import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from autosearchapp.models import Note
from autosearchapp.models import Vehicle
from .details import get_vehicle, create_vehicle
from ..connection import Connection



@login_required
def vehicle_form(request):
    if request.method == 'POST':
        vehicle = create_vehicle()
        template = 'vehicles/form.html'
        context = {
            'vehicles': vehicle,
        }

        return render(request, template, context)

@login_required
def vehicle_edit_form(request, vehicle_id):

    if request.method == 'GET':
        vehicle = get_vehicle(vehicle_id)

        template = 'vehicles/form.html'
        context = {
            'vehicle': vehicle,
        }

        return render(request, template, context)
