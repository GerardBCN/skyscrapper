from django.contrib import admin
from .models import TripTakeMeHome, TimeCheck, FlightDeparture, FlightReturn

# Register your models here.
admin.site.register(TripTakeMeHome)
admin.site.register(TimeCheck)
admin.site.register(FlightDeparture)
admin.site.register(FlightReturn)
