from django.contrib import admin
from .models import Trip, TimeSeries, PricePoint

admin.site.register(Trip)
admin.site.register(TimeSeries)
admin.site.register(PricePoint)

# Register your models here.
