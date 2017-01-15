from tracker.models import Trip
from takemehome.models import TripTakeMeHome
from django.shortcuts import render
import requests
from random import randint
from bs4 import BeautifulSoup
import unicodedata

def landing_page(request):
    trips = Trip.objects.order_by('published_date')
    TMH_trips = TripTakeMeHome.objects.order_by('published_date')
    return render(request, 'landing_page.html', {'trips': trips, 'takemehometrips':TMH_trips})

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def vueling_track_round_trip(trip):

    oneWay = trip.one_way
    #print(oneWay)

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

    ListMarketDay2, ListMarketMonth2, DateReturn = "", "", ""
    MarketStructure = "OneWay"
    if not (oneWay):
        ListMarketDay2= str(trip.date_return.day).zfill(2)
        ListMarketMonth2 = str(trip.date_return.year)+"-"+str(trip.date_return.month).zfill(2)
        MarketStructure = "RoundTrip"
        DateReturn = str(trip.date_return)

    # XMLsearch post
    params = {
        'AvailabilitySearchInputXmlSearchView$DropDownListMarketDay1':str(trip.date_departure.day).zfill(2),
        'AvailabilitySearchInputXmlSearchView$DropDownListMarketDay2':ListMarketDay2,
        'AvailabilitySearchInputXmlSearchView$DropDownListMarketMonth1':str(trip.date_departure.year)+"-"+str(trip.date_departure.month).zfill(2),
        'AvailabilitySearchInputXmlSearchView$DropDownListMarketMonth2':ListMarketMonth2,
        'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_ADT':'1',
        'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_CHD':'0',
        'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_INFANT':'0',
        'AvailabilitySearchInputXmlSearchView$DropDownListSearchBy':'columnView',
        'AvailabilitySearchInputXmlSearchView$ExtraSeat':'',
        'AvailabilitySearchInputXmlSearchView$RadioButtonMarketStructure':MarketStructure,
        'AvailabilitySearchInputXmlSearchView$ResidentFamNumSelector':'',
        'AvailabilitySearchInputXmlSearchView$TextBoxMarketDestination1':unicodedata.normalize('NFD', trip.get_destination_display()).encode('ascii', 'ignore'),
        'AvailabilitySearchInputXmlSearchView$TextBoxMarketOrigin1':unicodedata.normalize('NFD', trip.get_origin_display()).encode('ascii', 'ignore'),
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
        'arrivalStationCode1':str(trip.destination),
        'arrivalStationCode2':'',
        'date_picker':str(trip.date_departure),
        'date_picker':DateReturn,
        'departureStationCode1':str(trip.origin),
        'departureStationCode2':'',
        'pageToken':''
    }
    #print(params)
    posturl='https://tickets.vueling.com/XmlSearch.aspx'
    r = s.post(posturl, data=params, headers=headers_post, cookies=s.cookies)

    # scheduleselect get
    geturl='https://tickets.vueling.com/ScheduleSelect.aspx'
    r = s.get(geturl, headers=headers_post2, cookies=s.cookies)

    res = {}
    res['departure']=[]
    res['return']=[]

    try:
        html = BeautifulSoup(r.text,"html.parser")
        idas = html.find_all('table', {'id':'availabilityTable0'})[0].find_all("tbody")[0].find_all("tr")
        vueltas = ""
        if not (oneWay):
            vueltas = html.find_all('table', {'id':'availabilityTable1'})[0].find_all("tbody")[0].find_all("tr")
    except:
        return res

    for i,entrada in enumerate(idas):
        try:
            precio = entrada.find_all('td',{'class':['price', 'basictd']})[0].find('span', {'class' : 'wrapper_currency'}).getText()
            precio = precio.encode('ascii', 'ignore').replace(",",".")
            hora = entrada.find('span', {'class' : 'fs_14' }).getText()
            res['departure'].append([float(precio), hora])
        except:
            pass
        #print (i + 1, precio, hora)

    if not (oneWay):
        for i,entrada in enumerate(vueltas):
            try:
                precio = entrada.find_all('td',{'class':['price', 'basictd']})[0].find('span', {'class' : 'wrapper_currency'}).getText()
                precio = precio.encode('ascii', 'ignore').replace(",",".")
                hora = entrada.find('span', {'class' : 'fs_14' }).getText()
                res['return'].append([float(precio), hora])
            except:
                pass
            #print (i + 1, precio, hora)
    return res
