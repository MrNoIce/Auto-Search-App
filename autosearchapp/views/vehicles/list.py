import sqlite3
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from autosearchapp.models import Vehicle
from ..connection import Connection

@login_required
def vehicle_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            user = request.user
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                v.id,
                v.heading,
                v.mileage,
                v.color,
                v.vin,
                v.zip_code,
                v.vdp_url,
                v.price,
                v.user_id,
                n.vehicle_notes
            from autosearchapp_vehicle v
            LEFT JOIN autosearchapp_note n on vehicle_id = v.id
            WHERE user_id = ?
            """,(user.id,))

            saved_vehicles = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                vehicle = Vehicle()
                vehicle.id = row['id']
                vehicle.heading = row['heading']
                vehicle.mileage = row['mileage']
                vehicle.color = row['color']
                vehicle.vin = row['vin']
                vehicle.zip_code = row['zip_code']
                vehicle.vdp_url = row['vdp_url']
                vehicle.price = row['price']
                vehicle.user_id = row['user_id']
                vehicle.notes = row['vehicle_notes']

                saved_vehicles.append(vehicle)

        template = 'vehicles/list.html'
        context = {
            'saved_vehicles': saved_vehicles
        }

        return render(request, template, context)