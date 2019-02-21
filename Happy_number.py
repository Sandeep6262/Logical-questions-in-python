print "happy number"
user = str(raw_input("input any number"))
new_list = [ ]

while True:
	var = 0
	add = 0
	while var < len(user):
		b = int(user[var])
		c = b * b
		add+=c

		var+=1

	if add == 1:
		print "happy number"
		break
	else:
		if add in new_list:
			print "not happy number"
			break
		else:
			new_list.append(add)
			user = str(add)


