import requests

headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-GB,en;q=0.5',
	'Connection':'keep-alive',
	'Host':'tickets.vueling.com',
	'User-Agent':'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:33.0) Gecko/20100101 Firefox/33.0',
    'Referer':'http://www.vueling.com/es'
}

s = requests.session()

r = s.get('http://www.vueling.com/en', headers=headers ,verify=False)
#print(r.text)
print(r.cookies)

r = s.post('https://cgenff.paramchem.org/userAccount/userWelcome.php', cookies=cookie, headers=headers ,files=[('usrName',('',user)),('curPwd',('',password)),('rndNo',('',str(random_with_N_digits(9)))),('submitBtn',('','Submit'))], verify=False)

