import json
import urllib.request
import re
count = 0
lst = list()
nlst = list()
vlst = list()


url = input('URL:')
urldata = urllib.request.urlopen(url).read()


data = json.loads(urldata)

for k,v in data.items():
	nval = (k,v)
	vlst.append(nval)



for item in vlst:
	place = str(item)
	nlst.append(place)

for item in nlst:
	
	if isinstance(item, str):

		x = re.findall('[0-9]+', item)
		stop = len(x)
		if stop > 0:
	
			for i in range(stop):
				lst.append(int(x[i]))

		
		else:
			continue
	else:
		continue


for item in lst:
	count += item


print(count)