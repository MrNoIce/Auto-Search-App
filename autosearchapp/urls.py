from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from autosearchapp.models import *
from autosearchapp.views import *

app_name = "autosearchapp"


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', vehicle_list, name='home'),
    url(r'^vehicles$', vehicle_list, name='vehicles'),
    path('vehicle/<int:vehicle_id>/', vehicle_details, name='vehicle'),
    url(r'^vehicle/form$', vehicle_form, name='vehicle_form'),
    url(r'^vehicles/(?P<vehicle_id>[0-9]+)/editform$', vehicle_edit_form, name='vehicle_edit_form'),
]