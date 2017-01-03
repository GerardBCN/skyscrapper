import requests
import re

headers_get = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-GB,en;q=0.5',
	'Connection':'keep-alive',
	'Host':'tickets.vueling.com',
	'User-Agent':'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Referer':'http://www.vueling.com/es'
}

headers_get2 = {
    'Host': 'www.vueling.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'X-Requested-With': 'XMLHttpRequest',
    'Referer': 'http://www.vueling.com/en',
    'DNT': '1',
    'Connection': 'keep-alive'
}

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

# main page get
r = s.get('http://www.vueling.com/en', headers=headers_get)

# First cookie manager get
r = s.get('http://www.vueling.com/Base/CookieManager/GetCookieLastSearch', headers=headers_get2 , cookies=s.cookies)

#Render Macros get
params = {
    '_':'1483446752180',
    'callback':'loadMacrosNewHomeSuccess',
    'idioma':'en-GB',
    'macroalias':'DestacadosUltimaBusqueda,AreaPrivada,PersonalizedOffersCities,YouWillBePremium',
    'pageid':'4516',
    'userSelectedOrigin':'BCN'
}
r = s.get('https://www.vueling.com/Base/BaseProxy/RenderMacrosNC', params=params, cookies=s.cookies)

# XMLsearch post
params = {
    'AvailabilitySearchInputXmlSearchView$DropDownListMarketDay1':'03',
    'AvailabilitySearchInputXmlSearchView$DropDownListMarketDay2':'10',
    'AvailabilitySearchInputXmlSearchView$DropDownListMarketMonth1':'2017-01',
    'AvailabilitySearchInputXmlSearchView$DropDownListMarketMonth2':'2017-01',
    'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_ADT':'1',
    'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_CHD':'0',
    'AvailabilitySearchInputXmlSearchView$DropDownListPassengerType_INFANT':'0',
    'AvailabilitySearchInputXmlSearchView$DropDownListSearchBy':'columnView',
    'AvailabilitySearchInputXmlSearchView$ExtraSeat':'',
    'AvailabilitySearchInputXmlSearchView$RadioButtonMarketStructure':'RoundTrip',
    'AvailabilitySearchInputXmlSearchView$ResidentFamNumSelector':'',
    'AvailabilitySearchInputXmlSearchView$TextBoxMarketDestination1':'Moscow',
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
    'arrivalStationCode1':'MOW',
    'arrivalStationCode2':'',
    'date_picker':'2017-01-03',
    'date_picker':'2017-01-10',
    'departureStationCode1':'BCN',
    'departureStationCode2':'',
    'pageToken':''
}

posturl='https://tickets.vueling.com/XmlSearch.aspx'
r = s.post(posturl, data=params, headers=headers_post, cookies=s.cookies)
#print(r.text)

geturl='https://tickets.vueling.com/ScheduleSelect.aspx'
r = s.get(geturl, headers=headers_post2, cookies=s.cookies)
print(r.text)

p = re.compile('\"basicPriceRoute\":\"(.*)\"')
m = p.match(r.text)
m.group(0)
