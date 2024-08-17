import json
import re
import urllib
import urllib.request

serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

add = input("Enter location:")


dcode = add.strip()

vcode = urllib.request.urlopen(dcode).read()

print(vcode)

ddcode = json.loads(vcode)

print(ddcode)
print(type(ddcode))

url = serviceurl + ddcode
uh = urllib.request.urlopen(url)


data = uh.read().decode()

print(data)
print(type(data))



x = re.findall('[0-9A-Z]+[+][0-9A-Z]+', data)
plus_code = x[0]


print("Plus code = ", plus_code)