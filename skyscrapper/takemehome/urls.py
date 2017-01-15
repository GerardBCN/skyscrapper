from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trip/new/$', views.new_takeMeHome_trip, name='new_takeMeHome_trip'),
    url(r'^trip/(?P<pk>[0-9]+)/$', views.takeMeHomeTrip_detail, name='takeMeHomeTrip_detail'),
]
