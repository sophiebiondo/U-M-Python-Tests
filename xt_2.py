import xml.etree.ElementTree as ET
import urllib.request
count = 0


url = input('URL:')
urldata = urllib.request.urlopen(url).read()

rawdata = ET.fromstring(urldata)

elements = rawdata.findall('comments/comment/count')

print("Counts received:", str(len(elements)))

for item in elements:
	
	x = item.text
	count += int(x)
	



print(str(count))