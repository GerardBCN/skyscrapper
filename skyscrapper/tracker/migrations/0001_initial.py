# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PricePoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=3, max_digits=5)),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='TimeSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('origin', models.CharField(max_length=3)),
                ('destination', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(choices=[('LCG', 'A Coru\xf1a'), ('AAL', 'Aalborg'), ('ACC', 'Acra'), ('ALC', 'Alicante'), ('LEI', 'Almer\xeda'), ('AMS', '\xc1msterdam'), ('ALG', 'Argel'), ('OVD', 'Asturias (Oviedo)'), ('ATH', 'Atenas'), ('BJL', 'Banjul'), ('BCN', 'Barcelona'), ('BRI', 'Bari'), ('BSL', 'Basilea'), ('BIA', 'Bastia (C\xf3rcega)'), ('BEY', 'Beirut'), ('BEG', 'Belgrado'), ('BGO', 'Bergen'), ('TXL', 'Berl\xedn (Tegel)'), ('BIO', 'Bilbao'), ('BHX', 'Birmingham'), ('BLQ', 'Bolonia'), ('BES', 'Brest'), ('BDS', 'Br\xedndisi'), ('BRU', 'Bruselas'), ('OTP', 'Bucarest'), ('BUD', 'Budapest'), ('BOD', 'Burdeos'), ('CAG', 'Cagliari'), ('CWL', 'Cardiff'), ('CMN', 'Casablanca'), ('CTA', 'Catania'), ('EFL', 'Cefalonia'), ('CLJ', 'Cluj-Napoca'), ('CPH', 'Copenhague'), ('CFU', 'Corf\xfa'), ('KRK', 'Cracovia'), ('HER', 'Creta'), ('DKR', 'Dakar'), ('DUB', 'Dubl\xedn'), ('DBV', 'Dubrovnik'), ('DUS', 'D\xfcsseldorf'), ('EDI', 'Edimburgo'), ('EIN', 'Eindhoven'), ('ARN', 'Estocolmo'), ('FAO', 'Faro'), ('FEZ', 'Fez'), ('FLR', 'Florencia'), ('FRA', 'Frankfurt'), ('FUE', 'Fuerteventura'), ('GOA', 'G\xe9nova'), ('GVA', 'Ginebra'), ('GOT', 'Gotemburgo'), ('LPA', 'Gran Canaria'), ('GRX', 'Granada'), ('HAM', 'Hamburgo'), ('HAJ', 'Han\xf3ver'), ('HEL', 'Helsinki'), ('IBZ', 'Ibiza'), ('XRY', 'Jerez (C\xe1diz)'), ('KGD', 'Kaliningrado'), ('AOK', 'K\xe1rpatos'), ('IEV', 'Kiev'), ('KGS', 'Kos'), ('SPC', 'La Palma'), ('LMP', 'Lampedusa'), ('ACE', 'Lanzarote'), ('LCA', 'L\xe1rnaca'), ('LBA', 'Leeds'), ('LIL', 'Lille'), ('LIS', 'Lisboa'), ('LGW', 'Londres'), ('LHR', 'Londres (Heathrow)'), ('LTN', 'Londres (Luton)'), ('LUX', 'Luxemburgo'), ('LYS', 'Lyon'), ('FNC', 'Madeira'), ('MAD', 'Madrid'), ('AGP', 'M\xe1laga'), ('PMI', 'Mallorca'), ('MLA', 'Malta'), ('MAN', 'Manchester'), ('RAK', 'Marrakech'), ('MRS', 'Marsella'), ('MAH', 'Menorca'), ('JMK', 'Mikonos'), ('MXP', 'Mil\xe1n'), ('MSQ', 'Minsk'), ('DME', 'Mosc\xfa'), ('MUC', 'M\xfanich'), ('NDR', 'Nador'), ('NTE', 'Nantes'), ('NAP', 'N\xe1poles'), ('NCL', 'Newcastle'), ('NCE', 'Niza'), ('NUE', 'Nuremberg'), ('OLB', 'Olbia'), ('OPO', 'Oporto'), ('ORN', 'Or\xe1n'), ('OSL', 'Oslo'), ('PMO', 'Palermo'), ('CDG', 'Par\xeds'), ('ORY', 'Par\xeds (Orly)'), ('PSA', 'Pisa (Toscana)'), ('PRG', 'Praga'), ('PVK', 'Pr\xe9veza'), ('KEF', 'Reikiavik'), ('RNS', 'Rennes'), ('RHO', 'Rodas'), ('FCO', 'Roma (Fiumicino)'), ('RTM', 'R\xf3terdam'), ('LED', 'San Petersburgo'), ('EAS', 'San Sebasti\xe1n'), ('SDR', 'Santander'), ('SCQ', 'Santiago'), ('JTR', 'Santorini'), ('SVQ', 'Sevilla'), ('SPU', 'Split'), ('STR', 'Stuttgart'), ('TLL', 'Tallin'), ('TNG', 'T\xe1nger'), ('TLV', 'Tel Aviv'), ('TFN', 'Tenerife'), ('TFS', 'Tenerife Sur'), ('SKG', 'Tesal\xf3nica'), ('TLS', 'Toulouse'), ('TUN', 'T\xfanez'), ('TRN', 'Turin'), ('VLC', 'Valencia'), ('VLL', 'Valladolid'), ('WAW', 'Varsovia'), ('VCE', 'Venecia'), ('VRN', 'Verona'), ('VIE', 'Viena'), ('VGO', 'Vigo'), ('ZAD', 'Zadar'), ('ZAG', 'Zagreb'), ('ZTH', 'Zante'), ('ZAZ', 'Zaragoza'), ('ZRH', 'Z\xfarich')], max_length=3)),
                ('destination', models.CharField(choices=[('LCG', 'A Coru\xf1a'), ('AAL', 'Aalborg'), ('ACC', 'Acra'), ('ALC', 'Alicante'), ('LEI', 'Almer\xeda'), ('AMS', '\xc1msterdam'), ('ALG', 'Argel'), ('OVD', 'Asturias (Oviedo)'), ('ATH', 'Atenas'), ('BJL', 'Banjul'), ('BCN', 'Barcelona'), ('BRI', 'Bari'), ('BSL', 'Basilea'), ('BIA', 'Bastia (C\xf3rcega)'), ('BEY', 'Beirut'), ('BEG', 'Belgrado'), ('BGO', 'Bergen'), ('TXL', 'Berl\xedn (Tegel)'), ('BIO', 'Bilbao'), ('BHX', 'Birmingham'), ('BLQ', 'Bolonia'), ('BES', 'Brest'), ('BDS', 'Br\xedndisi'), ('BRU', 'Bruselas'), ('OTP', 'Bucarest'), ('BUD', 'Budapest'), ('BOD', 'Burdeos'), ('CAG', 'Cagliari'), ('CWL', 'Cardiff'), ('CMN', 'Casablanca'), ('CTA', 'Catania'), ('EFL', 'Cefalonia'), ('CLJ', 'Cluj-Napoca'), ('CPH', 'Copenhague'), ('CFU', 'Corf\xfa'), ('KRK', 'Cracovia'), ('HER', 'Creta'), ('DKR', 'Dakar'), ('DUB', 'Dubl\xedn'), ('DBV', 'Dubrovnik'), ('DUS', 'D\xfcsseldorf'), ('EDI', 'Edimburgo'), ('EIN', 'Eindhoven'), ('ARN', 'Estocolmo'), ('FAO', 'Faro'), ('FEZ', 'Fez'), ('FLR', 'Florencia'), ('FRA', 'Frankfurt'), ('FUE', 'Fuerteventura'), ('GOA', 'G\xe9nova'), ('GVA', 'Ginebra'), ('GOT', 'Gotemburgo'), ('LPA', 'Gran Canaria'), ('GRX', 'Granada'), ('HAM', 'Hamburgo'), ('HAJ', 'Han\xf3ver'), ('HEL', 'Helsinki'), ('IBZ', 'Ibiza'), ('XRY', 'Jerez (C\xe1diz)'), ('KGD', 'Kaliningrado'), ('AOK', 'K\xe1rpatos'), ('IEV', 'Kiev'), ('KGS', 'Kos'), ('SPC', 'La Palma'), ('LMP', 'Lampedusa'), ('ACE', 'Lanzarote'), ('LCA', 'L\xe1rnaca'), ('LBA', 'Leeds'), ('LIL', 'Lille'), ('LIS', 'Lisboa'), ('LGW', 'Londres'), ('LHR', 'Londres (Heathrow)'), ('LTN', 'Londres (Luton)'), ('LUX', 'Luxemburgo'), ('LYS', 'Lyon'), ('FNC', 'Madeira'), ('MAD', 'Madrid'), ('AGP', 'M\xe1laga'), ('PMI', 'Mallorca'), ('MLA', 'Malta'), ('MAN', 'Manchester'), ('RAK', 'Marrakech'), ('MRS', 'Marsella'), ('MAH', 'Menorca'), ('JMK', 'Mikonos'), ('MXP', 'Mil\xe1n'), ('MSQ', 'Minsk'), ('DME', 'Mosc\xfa'), ('MUC', 'M\xfanich'), ('NDR', 'Nador'), ('NTE', 'Nantes'), ('NAP', 'N\xe1poles'), ('NCL', 'Newcastle'), ('NCE', 'Niza'), ('NUE', 'Nuremberg'), ('OLB', 'Olbia'), ('OPO', 'Oporto'), ('ORN', 'Or\xe1n'), ('OSL', 'Oslo'), ('PMO', 'Palermo'), ('CDG', 'Par\xeds'), ('ORY', 'Par\xeds (Orly)'), ('PSA', 'Pisa (Toscana)'), ('PRG', 'Praga'), ('PVK', 'Pr\xe9veza'), ('KEF', 'Reikiavik'), ('RNS', 'Rennes'), ('RHO', 'Rodas'), ('FCO', 'Roma (Fiumicino)'), ('RTM', 'R\xf3terdam'), ('LED', 'San Petersburgo'), ('EAS', 'San Sebasti\xe1n'), ('SDR', 'Santander'), ('SCQ', 'Santiago'), ('JTR', 'Santorini'), ('SVQ', 'Sevilla'), ('SPU', 'Split'), ('STR', 'Stuttgart'), ('TLL', 'Tallin'), ('TNG', 'T\xe1nger'), ('TLV', 'Tel Aviv'), ('TFN', 'Tenerife'), ('TFS', 'Tenerife Sur'), ('SKG', 'Tesal\xf3nica'), ('TLS', 'Toulouse'), ('TUN', 'T\xfanez'), ('TRN', 'Turin'), ('VLC', 'Valencia'), ('VLL', 'Valladolid'), ('WAW', 'Varsovia'), ('VCE', 'Venecia'), ('VRN', 'Verona'), ('VIE', 'Viena'), ('VGO', 'Vigo'), ('ZAD', 'Zadar'), ('ZAG', 'Zagreb'), ('ZTH', 'Zante'), ('ZAZ', 'Zaragoza'), ('ZRH', 'Z\xfarich')], max_length=3)),
                ('date_departure', models.DateField()),
                ('date_return', models.DateField()),
                ('activated', models.BooleanField(default=True)),
                ('published_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='timeseries',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeseries', to='tracker.Trip'),
        ),
        migrations.AddField(
            model_name='pricepoint',
            name='timeseries',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pricepoints', to='tracker.TimeSeries'),
        ),
    ]
