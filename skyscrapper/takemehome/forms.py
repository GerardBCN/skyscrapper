from django import forms
from .models import TripTakeMeHome
from django.contrib.admin import widgets

class TripTakeMeHomeForm(forms.ModelForm):
    class Meta:
        model = TripTakeMeHome
        fields = ['origin', 'destination', 'start_week_day', 'max_budget', 'number_of_bank_holidays', 'minimum_stay_days', 'number_of_months_ahead']
