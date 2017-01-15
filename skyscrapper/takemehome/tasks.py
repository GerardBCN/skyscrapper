from __future__ import absolute_import, unicode_literals
import datetime
import pytz
from celery import shared_task
from skyscrapper.views import vueling_track_round_trip
from .models import TripTakeMeHome, TimeCheck, FlightDeparture, FlightReturn

def next_weekday_within_x_months(d, weekday, months_ahead):
    res = []
    max_days = 30*months_ahead
    num_days = 0
    cur_day = d
    while num_days < max_days-7:
        days_ahead = weekday - cur_day.weekday()
        if days_ahead <= 0: # Target day already happened this week
            days_ahead += 7
        res.append(cur_day + datetime.timedelta(days_ahead))
        cur_day = cur_day + datetime.timedelta(days_ahead)
        num_days += days_ahead
    return res

def get_dates_delta_plus_weekends(day, num_bank_holidays, min_days_stay):
    total_max_stay = num_bank_holidays
    week_day = day.weekday()
    if week_day+num_bank_holidays >=4:
        total_max_stay += 2
    deltas = range(min_days_stay-1, total_max_stay)
    dates_res = [day + datetime.timedelta(delta) for delta in deltas]
    return dates_res

@shared_task
def check_best_takemehome_deals():
    trips = TripTakeMeHome.objects.all()
    for trip in trips:
        tc = TimeCheck(trip=trip)
        #print(tc)
        tc.save()
        next_weekdays = next_weekday_within_x_months(datetime.date.today(), int(trip.start_week_day), trip.number_of_months_ahead)
        for wd in next_weekdays:
            trip.date_departure = wd
            res = vueling_track_round_trip(trip)
            #print(res)
            for flight in res["departure"]:
                price = flight[0]
                hour = int(flight[1][:2])
                minute = int(flight[1][3:5])
                time = datetime.datetime(trip.date_departure.year, trip.date_departure.month, trip.date_departure.day, hour, minute, tzinfo=pytz.UTC)
                flightname = str(time.hour)+":"+str(time.minute)+trip.origin
                fd = FlightDeparture(timecheck=tc, origin=trip.origin, destination=trip.destination, flightname=flightname, price=price, time=time)
                #print(fd)
                fd.save()

        all_fd = tc.flightsDeparture.order_by('price')
        num_departures_check = 10
        if len(all_fd)<num_departures_check:
            num_departures_check = len(all_fd)
        cheapest_fd = all_fd[0:num_departures_check]

        ori = trip.origin
        des = trip.destination
        trip.origin = des
        trip.destination = ori

        for fd in cheapest_fd:
            dates_lookup = get_dates_delta_plus_weekends(fd.time.date(), trip.number_of_bank_holidays, trip.minimum_stay_days)
            #print(fd, dates_lookup)
            for date_fr in dates_lookup:
                trip.date_departure = date_fr
                #print(trip.origin, trip.destination)
                res = vueling_track_round_trip(trip)
                #print(res)
                for flight in res["departure"]:
                    price = flight[0]
                    hour = int(flight[1][:2])
                    minute = int(flight[1][3:5])
                    time = datetime.datetime(trip.date_departure.year, trip.date_departure.month, trip.date_departure.day, hour, minute, tzinfo=pytz.UTC)
                    flightname = str(time.hour)+":"+str(time.minute)+trip.origin
                    fr = FlightReturn(flightdeparture=fd, origin=trip.origin, destination=trip.destination, flightname=flightname, price=price, time=time)
                    #print(fr)
                    fr.save()
