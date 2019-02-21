def evan_odd(user):
	second_user = user
	print "This is evan number"
	for i in range (3):
		if user%2==0:
			user-=2
		else:
			user-=1
		print user
	print "this is odd number"
	for j in range(3):
		if second_user%2==0:
			second_user+=1
		else:
			second_user+=2
		print second_user
evan_odd(int(raw_input("input any number  ")))