from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from autosearchapp.models import *
from autosearchapp.views import *

app_name = "autosearchapp"


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    # url(r'^search$', search, name='search'),
    url(r'^save_vehicle$', new_vehicle, name='save_vehicle'),
    url(r'^vehicles$', vehicle_list, name='vehicles'),
    url(r'^vehiclessearch$', search, name='search'),
    path('new_note/<int:vehicle_id>/', new_note, name='new_note'),
    path('vehicle/<int:vehicle_id>/', vehicle_details, name='vehicle'),
    url(r'^vehicle/form/(?P<vehicle_id>[0-9]+)$', vehicle_details, name='vehicle_details'),
    url(r'^vehicles/(?P<vehicle_id>[0-9]+)/editform$', vehicle_edit_form, name='vehicle_edit_form'),
]