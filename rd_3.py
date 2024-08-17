import re
find = input("Enter file name:")
file = open(find)
afile = list()
gfile = list()
num = 0


for line in file:
	line.rstrip()
	x = re.findall('[0-9]+', line)
	
	if x > list():
		afile.append(x)
	else:
		continue




print(afile)


for line in afile:

	for word in line:
		newghost = word.split()
		gfile.append(newghost)
		


for line in gfile:
	num += int(line[0])


print(str(num))