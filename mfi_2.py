fname = input("Enter file name: ")
file = open(fname)
count = 0
conf = 0
for line in file:
	if not line.startswith("X-DSPAM-Confidence:"):
		continue
	elif line.startswith("X-DSPAM-Confidence:"):
		strl = line[21:]
		num = float(strl)			
		conf = conf + num
		count = count + 1
	else:
		print("ERROR")
		
avg = conf / count    
print("Average spam confidence:", str(avg))
