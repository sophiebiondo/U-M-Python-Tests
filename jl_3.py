import json
import urllib.request
import urllib
import re
lst = list()
nlst = list()
vlst = list()


og_url = input("Please enter location: ")
og_url.strip()
of_url = dict()
of_url['q'] = og_url
en_url = urllib.parse.urlencode(of_url)

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

urldata = urllib.request.urlopen(serviceurl + en_url).read()

data = json.loads(urldata)

for k,v in data.items():
	nval = (k,v)
	vlst.append(nval)



for item in vlst:
	place = str(item)
	nlst.append(place)

for item in nlst:
	
	if isinstance(item, str):

		x = re.findall('[0-9A-Z]+[+][0-9A-Z]+', item)
		stop = len(x)
		if stop > 0:
	
			for i in range(stop):
				lst.append((x[i]))

		
		else:
			continue
	else:
		continue


print(lst[0])