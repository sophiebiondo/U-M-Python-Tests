import re
import urllib
import urllib.request
from bs4 import BeautifulSoup
ncount = 0


url = input("URL:")
count = int(input("count:"))
position = int(input("position:"))



urll = urllib.request.urlopen(url)
soup = BeautifulSoup(urll, 'html.parser')

hm = str(soup)




y = re.findall('http[^"]*', hm)


for i in range(0, count - 1):

	new = urllib.request.urlopen(y[position - 1])
	nsoup = BeautifulSoup(new, 'html.parser')
	
	nstr = str(nsoup)
	
	y = re.findall('http[^"]*', nstr)
	



lstr = y[position - 1]
done = re.findall('[A-Z][a-z]*', lstr)

print(done)