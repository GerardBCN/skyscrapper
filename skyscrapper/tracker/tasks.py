# Create your tasks here
from __future__ import absolute_import, unicode_literals
import datetime
import pytz
from celery import shared_task
from skyscrapper.views import vueling_track_round_trip
from .models import Trip, PricePoint


@shared_task
def check_current_flight_prices():
    trips = Trip.objects.all()
    for trip in trips:
        if not trip.activated:
            continue
        res = vueling_track_round_trip(trip)
        for flight in res["departure"]:
            price = flight[0]
            hour = int(flight[1][:2])
            minute = int(flight[1][3:5])
            time = datetime.datetime(trip.date_departure.year, trip.date_departure.month, trip.date_departure.day, hour, minute, tzinfo=pytz.UTC)
            flightname = str(time.hour)+":"+str(time.minute)+trip.origin
            ts = trip.timeseries.get(flightname=flightname)
            pp = PricePoint(price=price, timeseries=ts)
            pp.save()
        if not (trip.one_way):
            for flight in res["return"]:
                price = flight[0]
                hour = int(flight[1][:2])
                minute = int(flight[1][3:5])
                time = datetime.datetime(trip.date_departure.year, trip.date_departure.month, trip.date_departure.day, hour, minute, tzinfo=pytz.UTC)
                flightname = str(time.hour)+":"+str(time.minute)+trip.destination
                ts = trip.timeseries.get(flightname=flightname)
                pp = PricePoint(price=price, timeseries=ts)
                pp.save()
