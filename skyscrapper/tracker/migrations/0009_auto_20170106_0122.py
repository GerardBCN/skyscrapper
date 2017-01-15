# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_timeseries_isreturn'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeseries',
            name='flightname',
            field=models.CharField(default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='pricepoint',
            name='price',
            field=models.DecimalField(decimal_places=5, max_digits=10),
        ),
    ]
