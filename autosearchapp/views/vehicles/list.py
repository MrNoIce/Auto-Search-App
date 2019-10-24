import sqlite3
from django.shortcuts import render
from autosearchapp.models import Vehicle
from ..connection import Connection


def vehicle_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select
                v.id,
                v.make,
                v.model,
                v.year,
                v.mileage,
                v.color,
                v.vin,
                v.zip_code,
                v.url,
                v.price,
                n.vehicle_notes
            from autosearchapp_vehicle v
            JOIN autosearchapp_note n WHERE vehicle_id = v.id;
            """)

            all_vehicles = []
            dataset = db_cursor.fetchall()

            for row in dataset:
                vehicle = Vehicle()
                vehicle.id = row['id']
                vehicle.make = row['make']
                vehicle.model = row['model']
                vehicle.year = row['year']
                vehicle.mileage = row['mileage']
                vehicle.color = row['color']
                vehicle.vin = row['vin']
                vehicle.zip_code = row['zip_code']
                vehicle.url = row['url']
                vehicle.price = row['price']

                all_vehicles.append(vehicle)

        template = 'vehicles/list.html'
        context = {
            'all_vehicles': all_vehicles
        }

        return render(request, template, context)