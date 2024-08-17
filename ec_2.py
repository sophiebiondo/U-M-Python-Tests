handle = input("Enter file name:")
file = open(handle)
emailnm = dict()


for line in file:
	if line.startswith("From "):
		create = line.split()
		email = create[1]
		if email in emailnm:
			emailnm[email] += 1
		else:
			emailnm[email] = 1
	else:
		continue

for email in emailnm:
	if email in emailnm == True:
		emailnm[email] = emailnm[email] + 1
	else:
		continue




highestnum = max(emailnm.values())
for email, count in emailnm.items():
	if count == highestnum:
		ghostnm = email
	else:
		continue


	
print(ghostnm, str(highestnum))
