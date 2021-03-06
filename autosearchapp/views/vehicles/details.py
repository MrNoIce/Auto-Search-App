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
        # gets one specific vehcile in the database
        db_cursor.execute("""
        SELECT
            v.id vehicle_id,
            v.heading,
            v.mileage,
            v.color,
            v.vin,
            v.zip_code,
            v.vdp_url,
            v.price,
            n.vehicle_notes
        from autosearchapp_vehicle v
        LEFT JOIN autosearchapp_note n ON vehicle_id = v.id
        WHERE v.id = ?
        """, (vehicle_id,))

        return db_cursor.fetchone()

@login_required
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
                UPDATE autosearchapp_note
                SET vehicle_notes = ?
                WHERE vehicle_id = ?
                """,
                (
                    form_data['vehicle_notes'], vehicle_id,
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
        # Builds vehicle() in order to get values in and out of for the data transfer from django to the db
    vehicle = Vehicle()
    vehicle.id = _row["vehicle_id"]
    vehicle.heading = _row["heading"]
    vehicle.color = _row["color"]
    vehicle.vin = _row["vin"]
    vehicle.zip_code = _row["zip_code"]
    vehicle.vdp_url = _row["vdp_url"]
    vehicle.price = _row["price"]

    note = Note()
    note.vehicle_notes = _row["vehicle_notes"]

    vehicle.note = note


    return vehicle