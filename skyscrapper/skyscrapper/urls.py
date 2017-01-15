from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.landing_page, name="landing_page"),
    url(r'^tracker/', include('tracker.urls')),
    url(r'^takemehome/', include('takemehome.urls')),
    url(r'^admin/', admin.site.urls),
]
