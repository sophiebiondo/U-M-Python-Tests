import urllib.request
import re
import urllib
from bs4 import BeautifulSoup


url = input('Enter - ')


urll = urllib.request.urlopen(url)
soup = BeautifulSoup(urll, 'html.parser')


unencrypted = str(soup)

y = re.findall('[0-9]+', unencrypted)
g = list()
r = 0
for line in y:
	if line != None:
		g.append(line)
	elif line > list():
		g.append(line)
	elif int(line) > 0:
		g.append(line)
	else: 
		continue 

for line in g:
	r += int(line)
r = r- 8
print(str(r))