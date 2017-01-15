from django import forms
from .models import Trip
from django.contrib.admin import widgets

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['origin', 'destination', 'date_departure', 'date_return', 'one_way']
