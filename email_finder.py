fname = input("Enter file name: ")
fh = open(fname)
count = 0
bear = list()
for line in fh:
	if line.startswith("From "):
		bear = line.split()
		print(bear[1])
		count  = count + 1
		continue
	else:
		continue
print("There were", str(count), "lines in the file with From as the first word")