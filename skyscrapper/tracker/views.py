from django.http import HttpResponse
import requests
from random import randint
from bs4 import BeautifulSoup
from .forms import TripForm
from django.shortcuts import render
from .models import Trip

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def trip_new(request):
    form = TripForm()
    return render(request, 'tracker/trip_edit.html', {'form': form})


def trip_list(request):
    return render(request, 'tracker/trip_list.html', {})

def create_trip(origin, destination, date_departure, date_return):

    #from datetime import date
    #example_date = date(2007, 12, 5)
    t = Trip(origin=origin, destination=destination, date_departure=date_departure, date_return=date_return)
    t.save()

def vueling_track(trip):

    headers_post = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'content-type':'application/x-www-form-urlencoded',
        'DNT':	'1',
        'Host':	'tickets.vueling.com',
        'Referer':'http://www.vueling.com/en',
        'Upgrade-Insecure-Requests'	:'1',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0'
    }

    headers_post2 = {
        'Host': 'tickets.vueling.com',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'http://www.vueling.com/en',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    s = requests.session()
    params = {
        '_':str(random_with_N_digits(13)),
        'callback':'loadMacrosNewHomeSuccess',
        'idioma':'en-GB',
        'macroalias':'DestacadosUltimaBusqueda,AreaPrivada,PersonalizedOffersCities,YouWillBePremium',
        'pageid':'4516',
        'userSelectedOrigin':'BCN'
    }
    r = s.get('https://www.vueling.com/Base/BaseProxy/RenderMacrosNC', params=params, cookies=s.cookies)

    # XMLsearch post
    params = {
        'AvailabilitySearchInputXmlSearchView$DropDownListMarketDay1':'09',
        'AvailabilitySearchInputXmlSearchView$DropDownListMarketDay2':'11',
        'AvailabilitySearchInputXmlSearchView$DropDownListMarketMonth1':'2017-02',
        'AvailabilitySearchInputXmlSearchView$DropDownListMarketMonth2':'2017-03',
        'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_ADT':'1',
        'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_CHD':'0',
        'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_INFANT':'0',
        'AvailabilitySearchInputXmlSearchView$DropDownListSearchBy':'columnView',
        'AvailabilitySearchInputXmlSearchView$ExtraSeat':'',
        'AvailabilitySearchInputXmlSearchView$RadioButtonMarketStructure':'RoundTrip',
        'AvailabilitySearchInputXmlSearchView$ResidentFamNumSelector':'',
        'AvailabilitySearchInputXmlSearchView$TextBoxMarketDestination1':'Munich',
        'AvailabilitySearchInputXmlSearchView$TextBoxMarketOrigin1':'Barcelona',
        'ErroneousWordDestination1':'',
        'ErroneousWordDestination2':'',
        'ErroneousWordOrigin1':'',
        'ErroneousWordOrigin2':'',
        'SelectedSuggestionDestination1':'',
        'SelectedSuggestionDestination2':'',
        'SelectedSuggestionOrigin1':'',
        'SelectedSuggestionOrigin2':'',
        '__EVENTARGUMENT':'',
        '__EVENTTARGET':'AvailabilitySearchInputXmlSearchView$LinkButtonNewSearch',
        '__VIEWSTATE':'/wEPDwUBMGRkTwRPn7sQIfLX6/slb1QXByDT65c=',
        'arrivalStationCode1':'MUC',
        'arrivalStationCode2':'',
        'date_picker':'2017-02-09',
        'date_picker':'2017-03-11',
        'departureStationCode1':'BCN',
        'departureStationCode2':'',
        'pageToken':''
    }
    posturl='https://tickets.vueling.com/XmlSearch.aspx'
    r = s.post(posturl, data=params, headers=headers_post, cookies=s.cookies)

    # scheduleselect get
    geturl='https://tickets.vueling.com/ScheduleSelect.aspx'
    r = s.get(geturl, headers=headers_post2, cookies=s.cookies)


    html = BeautifulSoup(r.text,"html.parser")
    idas = html.find_all('table', {'id':'availabilityTable0'})[0].find_all("tbody")[0].find_all("tr")
    vueltas = html.find_all('table', {'id':'availabilityTable1'})[0].find_all("tbody")[0].find_all("tr")

    print("Precios IDA")
    for i,entrada in enumerate(idas):
        precio = entrada.find_all('td',{'class':['price', 'basictd']})[0].find('span', {'class' : 'wrapper_currency'}).getText()
        hora = entrada.find('span', {'class' : 'fs_14' }).getText()
        print (i + 1, precio, hora)

    print("Precios VUELTA")
    for i,entrada in enumerate(vueltas):
        precio = entrada.find_all('td',{'class':['price', 'basictd']})[0].find('span', {'class' : 'wrapper_currency'}).getText()
        hora = entrada.find('span', {'class' : 'fs_14' }).getText()
        print (i + 1, precio, hora)
