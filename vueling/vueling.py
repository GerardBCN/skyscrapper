import requests

headers_get = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-GB,en;q=0.5',
	'Connection':'keep-alive',
	'Host':'tickets.vueling.com',
	'User-Agent':'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Referer':'http://www.vueling.com/es'
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

s = requests.session()

r = s.get('http://www.vueling.com/en', headers=headers_get ,verify=False)
#print(r.text)
print(r.cookies)

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
print(r.text)


