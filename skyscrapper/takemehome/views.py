from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from skyscrapper.views import vueling_track_round_trip
from .models import TripTakeMeHome, TimeCheck, FlightDeparture, FlightReturn
from takemehome.forms import TripTakeMeHomeForm
import datetime
import pytz

def new_takeMeHome_trip(request):
    if request.method == "POST":
        form = TripTakeMeHomeForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.save()
            return HttpResponseRedirect('/')
    else:
        form = TripTakeMeHomeForm()
    return render(request, 'takemehome/trip_new.html', {'form':form})



def takeMeHomeTrip_detail(request, pk):
    trip = TripTakeMeHome.objects.get(pk=pk)
    tc = trip.timechecks.order_by('timestamp').reverse()[0]

    all_fd = tc.flightsDeparture.order_by('price')
    num_departures_check = 10
    if len(all_fd)<num_departures_check:
        num_departures_check = len(all_fd)
    cheapest_fd = all_fd[0:num_departures_check]

    ori = trip.origin
    des = trip.destination

    cheapest_trips = []
    for fd in cheapest_fd:
        fr = fd.flightsReturn.order_by('price')[0]
        cheapest_trips.append([fd, fr, fd.price+fr.price])

    trip_info = [ori, des]

    return render(request, 'takemehome/trip_detail.html', {'ct':cheapest_trips, 'trip_info': trip_info, 'last_check_time':tc.timestamp})
