def divisible(user):
	for i in range(1,user+1):
		if i % 3 == 0 or i % 5 == 0:
			print i

divisible(int(raw_input("Enter number ")))