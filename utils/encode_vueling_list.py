from bs4 import BeautifulSoup
import re
f = open("./vueling_locals_raw.txt","r")
f2 = open("./vueling_locals.txt","w")
for line in f:
	mylin = BeautifulSoup(line).getText()
	#print(mylin)
	val = re.search(".*value=\"(.*?)\".*",line)
	print("('{}','{}'),".format(val.group(1),mylin.encode('utf-8').strip()))
	f2.write("('{}','{}'),\n".format(val.group(1),mylin.encode('utf-8').strip()))
f.close()
f2.close()
