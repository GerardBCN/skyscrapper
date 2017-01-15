from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^trip/(?P<pk>[0-9]+)/$', views.trip_detail, name='trip_detail'),
    url(r'^trip/new/$', views.trip_new, name='trip_new'),
]
