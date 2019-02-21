
def leapyear(user):
	fist_user = user-1
	print "this is three leap year back"
	add = 0
	while fist_user > 0:
		if add == 3:
			break
		elif fist_user % 4 == 0 and fist_user % 100 != 0:
			print fist_user
			add = add+1
		elif fist_user % 4 == 0 and fist_user % 100 == 0 and fist_user % 400 == 0:
			print fist_user
			add = add+1

		fist_user = fist_user - 1

	second_user = user+1
	sum1 = 0
	print "this is three leap year frant"
	var = 0
	while var < second_user:
		if sum1 == 3:
			break
		elif second_user % 4 == 0 and second_user % 100 != 0:
			print second_user
			sum1 = sum1+1
		elif second_user % 4 == 0 and second_user % 100 == 0 and second_user % 400 == 0:
			print second_user
			sum1 = sum1+1

		second_user = second_user+1



leapyear(int(raw_input("input any yera  ")))
