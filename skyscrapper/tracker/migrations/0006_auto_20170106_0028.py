# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-06 00:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20170106_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricepoint',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 6, 0, 28, 27, 552412, tzinfo=utc)),
        ),
    ]
