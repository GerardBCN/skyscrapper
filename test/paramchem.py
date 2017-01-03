import requests
from requests.auth import HTTPBasicAuth
import sys
from random import randint
import warnings
warnings.filterwarnings("ignore")
import xml.etree.ElementTree as ET
import re


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def printproc(process):
	sys.stdout.write(process)
	sys.stdout.flush()
def printok():
	sys.stdout.write("OK\n")


try:
	filepath = sys.argv[1]
	fileoutput = sys.argv[2]
	
except:
	print("Usage: paramchem <input_mol> <output_folder>")
	exit(0)


f = open('/shared/gerard/software/paramchem_api/auth.txt','r')
user = f.readline().strip()
password = f.readline().strip()
f.close()

headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Encoding':'gzip, deflate',
	'Accept-Language':'en-GB,en;q=0.5',
	'Connection':'keep-alive',
	'Host':'cgenff.paramchem.org',
	'User-Agent':'Mozilla/5.0 (X11; Linux i686 on x86_64; rv:33.0) Gecko/20100101 Firefox/33.0'
}

s = requests.session()

printproc("Retrieving a cookie sessionid... ")
r = s.get('https://cgenff.paramchem.org/userAccount/userLogin.php', headers=headers ,verify=False)
cookie = {'PHPSESSID':r.cookies['PHPSESSID']}
printok()

printproc("Activating session... ")
r = s.post('https://cgenff.paramchem.org/userAccount/userWelcome.php', cookies=cookie, headers=headers ,files=[('usrName',('',user)),('curPwd',('',password)),('rndNo',('',str(random_with_N_digits(9)))),('submitBtn',('','Submit'))], verify=False)
printok()

printproc("Checking job limit for this account... \n")
r = s.post('https://cgenff.paramchem.org/initguess/processdata.php', verify=False,cookies=cookie, data={'reqtype':'count'})
print(r.text.strip().split(';')[1])

printproc("Sending ligand in path \""+filepath+"\"... \n")
r = requests.post('https://cgenff.paramchem.org/initguess/processdata.php', verify=False,cookies=cookie, files=[('filename',('ligand.mol2',open(filepath,'rb'),'chemical/x-mol2')),('param_a',('','a'))])
try:
	root = ET.fromstring(r.text.strip())
	print('\tMessage: '+str(root.find('message').text))
	print('\tError: '+str(root.find('error').text))
	print('\tErrinfo: '+str(root.find('errinfo').text))
	print('\tPath: '+str(root.find('path').text))
	print('\tInput: '+str(root.find('input').text))
	print('\tOutput: '+str(root.find('output').text))

	resultpath = root.find('path').text
	outputname = root.find('output').text
except:
	print("SOME ERROR OCURRED. ABORTING!")
	exit(0)

printproc("Retrieving results... ")
r = s.get('https://cgenff.paramchem.org/initguess/filedownload.php?file='+str(resultpath)+'/'+str(outputname),verify=False,auth=HTTPBasicAuth(user,password),cookies=cookie)
strfile = r.text
if (strfile.startswith("* Toppar stream file generated by")):
	resicorrect = re.sub("RESI .{6}","RESI MOL   ", strfile)
	lines = resicorrect.split("\n")
	read_rtf = False
	read_prm = False
	rtf = ''
	prm = ''
	for line in lines:
		if line.startswith("* Topologies generated by"):
			read_rtf = True
			continue
		if line.startswith("* Parameters generated by"):
			read_prm = True
			continue
		if (read_rtf):
			rtf += line+"\n"
		if (read_prm):
			prm += line+"\n"
		if line.startswith("END"):
			read_rtf = False
			read_prm = False
	
	f = open(fileoutput+"/ff.rtf", "w")
	f.write(rtf)
	f.close()

	f = open(fileoutput+"/ff.prm","w")
	f.write(prm)
	f.close()

	printok()
	print("SUCCESS!")
else:
	print("SOME ERROR OCURRED. ABORTING!")
	exit(0)