# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator


LOCALS = (
    ('LCG','A Coruña'),
    ('AAL','Aalborg'),
    ('ACC','Acra'),
    ('ALC','Alicante'),
    ('LEI','Almería'),
    ('AMS','Ámsterdam'),
    ('ALG','Argel'),
    ('OVD','Asturias (Oviedo)'),
    ('ATH','Atenas'),
    ('BJL','Banjul'),
    ('BCN','Barcelona'),
    ('BRI','Bari'),
    ('BSL','Basilea'),
    ('BIA','Bastia (Córcega)'),
    ('BEY','Beirut'),
    ('BEG','Belgrado'),
    ('BGO','Bergen'),
    ('TXL','Berlín (Tegel)'),
    ('BIO','Bilbao'),
    ('BHX','Birmingham'),
    ('BLQ','Bolonia'),
    ('BES','Brest'),
    ('BDS','Bríndisi'),
    ('BRU','Bruselas'),
    ('OTP','Bucarest'),
    ('BUD','Budapest'),
    ('BOD','Burdeos'),
    ('CAG','Cagliari'),
    ('CWL','Cardiff'),
    ('CMN','Casablanca'),
    ('CTA','Catania'),
    ('EFL','Cefalonia'),
    ('CLJ','Cluj-Napoca'),
    ('CPH','Copenhague'),
    ('CFU','Corfú'),
    ('KRK','Cracovia'),
    ('HER','Creta'),
    ('DKR','Dakar'),
    ('DUB','Dublín'),
    ('DBV','Dubrovnik'),
    ('DUS','Düsseldorf'),
    ('EDI','Edimburgo'),
    ('EIN','Eindhoven'),
    ('ARN','Estocolmo'),
    ('FAO','Faro'),
    ('FEZ','Fez'),
    ('FLR','Florencia'),
    ('FRA','Frankfurt'),
    ('FUE','Fuerteventura'),
    ('GOA','Génova'),
    ('GVA','Ginebra'),
    ('GOT','Gotemburgo'),
    ('LPA','Gran Canaria'),
    ('GRX','Granada'),
    ('HAM','Hamburgo'),
    ('HAJ','Hanóver'),
    ('HEL','Helsinki'),
    ('IBZ','Ibiza'),
    ('XRY','Jerez (Cádiz)'),
    ('KGD','Kaliningrado'),
    ('AOK','Kárpatos'),
    ('IEV','Kiev'),
    ('KGS','Kos'),
    ('SPC','La Palma'),
    ('LMP','Lampedusa'),
    ('ACE','Lanzarote'),
    ('LCA','Lárnaca'),
    ('LBA','Leeds'),
    ('LIL','Lille'),
    ('LIS','Lisboa'),
    ('LGW','Londres'),
    ('LHR','Londres (Heathrow)'),
    ('LTN','Londres (Luton)'),
    ('LUX','Luxemburgo'),
    ('LYS','Lyon'),
    ('FNC','Madeira'),
    ('MAD','Madrid'),
    ('AGP','Málaga'),
    ('PMI','Mallorca'),
    ('MLA','Malta'),
    ('MAN','Manchester'),
    ('RAK','Marrakech'),
    ('MRS','Marsella'),
    ('MAH','Menorca'),
    ('JMK','Mikonos'),
    ('MXP','Milán'),
    ('MSQ','Minsk'),
    ('DME','Moscú'),
    ('MUC','Múnich'),
    ('NDR','Nador'),
    ('NTE','Nantes'),
    ('NAP','Nápoles'),
    ('NCL','Newcastle'),
    ('NCE','Niza'),
    ('NUE','Nuremberg'),
    ('OLB','Olbia'),
    ('OPO','Oporto'),
    ('ORN','Orán'),
    ('OSL','Oslo'),
    ('PMO','Palermo'),
    ('CDG','París'),
    ('ORY','París (Orly)'),
    ('PSA','Pisa (Toscana)'),
    ('PRG','Praga'),
    ('PVK','Préveza'),
    ('KEF','Reikiavik'),
    ('RNS','Rennes'),
    ('RHO','Rodas'),
    ('FCO','Roma (Fiumicino)'),
    ('RTM','Róterdam'),
    ('LED','San Petersburgo'),
    ('EAS','San Sebastián'),
    ('SDR','Santander'),
    ('SCQ','Santiago'),
    ('JTR','Santorini'),
    ('SVQ','Sevilla'),
    ('SPU','Split'),
    ('STR','Stuttgart'),
    ('TLL','Tallin'),
    ('TNG','Tánger'),
    ('TLV','Tel Aviv'),
    ('TFN','Tenerife'),
    ('TFS','Tenerife Sur'),
    ('SKG','Tesalónica'),
    ('TLS','Toulouse'),
    ('TUN','Túnez'),
    ('TRN','Turin'),
    ('VLC','Valencia'),
    ('VLL','Valladolid'),
    ('WAW','Varsovia'),
    ('VCE','Venecia'),
    ('VRN','Verona'),
    ('VIE','Viena'),
    ('VGO','Vigo'),
    ('ZAD','Zadar'),
    ('ZAG','Zagreb'),
    ('ZTH','Zante'),
    ('ZAZ','Zaragoza'),
    ('ZRH','Zúrich'),
)

DAYS_OF_WEEK = (
    ('0', 'Monday'),
    ('1', 'Tuesday'),
    ('2', 'Wednesday'),
    ('3', 'Thursday'),
    ('4', 'Friday'),
    ('5', 'Saturday'),
    ('6', 'Sunday'),
)


class TripTakeMeHome(models.Model):
    origin = models.CharField(max_length=3, choices=LOCALS)
    destination = models.CharField(max_length=3, choices=LOCALS)
    start_week_day = models.CharField(max_length=1, default=4, choices=DAYS_OF_WEEK)
    max_budget = models.IntegerField(default=70)
    number_of_bank_holidays = models.IntegerField(default=4, validators=[MaxValueValidator(10),MinValueValidator(1)])
    minimum_stay_days = models.IntegerField(default=4, validators=[MaxValueValidator(10),MinValueValidator(2)])
    number_of_months_ahead = models.IntegerField(default=3, validators=[MaxValueValidator(6),MinValueValidator(1)])
    activated = models.BooleanField(default=True)
    date_departure = models.DateField(default=datetime.date.today)
    date_return = models.DateField(default=datetime.date.today)
    published_date = models.DateTimeField(auto_now_add = True)
    one_way = models.BooleanField(default=True)
    def __str__(self):
        return "{}-{} {}/{}".format(self.origin,self.destination,self.start_week_day, self.max_budget)

class TimeCheck(models.Model):
    trip = models.ForeignKey(TripTakeMeHome, related_name="timechecks")
    timestamp = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['timestamp']
    def __str__(self):
        return "{} parent:{}".format(self.timestamp, self.trip)

class FlightDeparture(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    flightname = models.CharField(max_length=20, default="NA")
    price = models.DecimalField(max_digits=10, decimal_places=5)
    time = models.DateTimeField()
    timecheck = models.ForeignKey(TimeCheck, related_name="flightsDeparture")
    def __str__(self):
        return "{} {} {}".format(self.flightname,self.price, self.time)

class FlightReturn(models.Model):
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    flightname = models.CharField(max_length=20, default="NA")
    price = models.DecimalField(max_digits=10, decimal_places=5)
    time = models.DateTimeField()
    flightdeparture = models.ForeignKey(FlightDeparture, related_name="flightsReturn")
    def __str__(self):
        return "{} {} {}".format(self.flightname,self.price, self.time)
