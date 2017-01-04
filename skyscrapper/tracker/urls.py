from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.trip_list, name='trip_list'),
    url(r'^trip/new/$', views.trip_new, name='trip_new'),
]
