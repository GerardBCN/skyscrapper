from django.http import HttpResponse, HttpResponseRedirect
from tracker.forms import TripForm
from django.shortcuts import render, redirect
from tracker.models import Trip, TimeSeries, PricePoint
from skyscrapper.views import vueling_track_round_trip
import datetime
import pytz

def trip_new(request):
    if request.method == "POST":
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            res = vueling_track_round_trip(trip)
            for flight in res["departure"]:
                price = flight[0]
                hour = int(flight[1][:2])
                minute = int(flight[1][3:5])
                time = datetime.datetime(trip.date_departure.year, trip.date_departure.month, trip.date_departure.day, hour, minute, tzinfo=pytz.UTC)
                flightname = str(time.hour)+":"+str(time.minute)+trip.origin
                ts = TimeSeries(trip=trip, time=time, origin=trip.origin, destination=trip.destination, flightname=flightname)
                ts.save()
                pp = PricePoint(price=price, timeseries=ts)
                pp.save()
            if not (trip.one_way):
                for flight in res["return"]:
                    price = flight[0]
                    hour = int(flight[1][:2])
                    minute = int(flight[1][3:5])
                    time = datetime.datetime(trip.date_departure.year, trip.date_departure.month, trip.date_departure.day, hour, minute, tzinfo=pytz.UTC)
                    flightname = str(time.hour)+":"+str(time.minute)+trip.destination
                    ts = TimeSeries(trip=trip, time=time, origin=trip.destination, destination=trip.origin, isreturn=True, flightname=flightname)
                    ts.save()
                    pp = PricePoint(price=price, timeseries=ts)
                    pp.save()
            return HttpResponseRedirect('/')
    else:
        form = TripForm()
    return render(request, 'tracker/trip_edit.html', {'form': form})



def trip_detail(request, pk):
    trip = Trip.objects.get(pk=pk)
    timeseries = trip.timeseries.all()
    res = {}
    res["departure"] = {}
    res["return"] = {}
    res["return"]['flightnames']=[]
    res["departure"]['flightnames']=[]
    for ts in timeseries:
        flightname = ts.flightname
        pricepoints = ts.pricepoints.all()
        if (ts.isreturn):
            res["return"]['flightnames'].append(flightname)
            if not "values" in res["return"]:
                res["return"]["values"]=[["new Date({},{},{},{},{})".format(pp.timestamp.year,pp.timestamp.month,pp.timestamp.day,pp.timestamp.hour,pp.timestamp.minute)] for pp in pricepoints]
            for i,pp in enumerate(pricepoints):
                res["return"]["values"][i].append(pp.price)
        else:
            res["departure"]['flightnames'].append(flightname)
            if not "values" in res["departure"]:
                res["departure"]["values"]=[["new Date({},{},{},{},{})".format(pp.timestamp.year,pp.timestamp.month,pp.timestamp.day,pp.timestamp.hour,pp.timestamp.minute)] for pp in pricepoints]
            for i,pp in enumerate(pricepoints):
                res["departure"]["values"][i].append(pp.price)
    #print(res)
    return render(request, 'tracker/trip_detail.html', {'flights':res, 'trip':trip})
