import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from autosearchapp.models import Note
from autosearchapp.models import Vehicle
from autosearchapp.models import model_factory
from ..connection import Connection


def get_vehicle(vehicle_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_vehicle
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            v.id vehicle_id,
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
        JOIN autosearchapp_note n ON vehicle_id = v.id
        WHERE v.id = ?
        """, (vehicle_id,))

        return db_cursor.fetchone()

# @login_required
def vehicle_details(request, vehicle_id):
    if request.method == 'GET':
        vehicle = get_vehicle(vehicle_id)
        template_name = 'vehicles/detail.html'
        return render(request, template_name, {'vehicle': vehicle})

    elif request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a vehicle
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE autosearchapp_vehicle
                SET make = ?,
                    model = ?,
                    year = ?,
                    mileage = ?,
                    color = ?
                WHERE id = ?
                """,
                (
                    form_data['make'], form_data['model'],
                    form_data['year'], form_data['mileage'],
                    form_data["color"],form_data["vin"],
                    form_data["zip_code"],form_data["url"],
                    form_data["price"], vehicle_id,
                ))

            return redirect(reverse('autosearchapp:vehicles'))

        # Check if this POST is for deleting a vehicle
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                    DELETE FROM autosearchapp_vehicle
                    WHERE id = ?
                """, (vehicle_id,))

            return redirect(reverse('autosearchapp:vehicles'))

def create_vehicle(cursor, row):
    _row = sqlite3.Row(cursor, row)

    vehicle = Vehicle()
    vehicle.id = _row["vehicle_id"]
    vehicle.make = _row["make"]
    vehicle.model = _row["model"]
    vehicle.year = _row["year"]
    vehicle.color = _row["color"]
    vehicle.vin = _row["vin"]
    vehicle.zip_code = _row["zip_code"]
    vehicle.url = _row["url"]
    vehicle.price = _row["price"]

    note = Note()
    note.vehicle_notes = _row["vehicle_notes"]

    vehicle.note = note


    return vehicle