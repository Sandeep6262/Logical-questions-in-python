def armstrong(user):
	for i in range (1,user+1):
		a = str(i)
		add = 0
		for j in a:
			b = int(j)
			k = b**3
			add=add+k

		if add == int(a):
			print a


armstrong(int(raw_input("input any number  ")))

# user = int(raw_input("Enter number  "))
# # user1 = int(user)
# for i in range(1,user+1):
# 	k = str(i)
# 	add = 0
# 	for j in k:
# 		l = int(j)
# 		k = l**3
# 		add+=k
# 	if add == int(i):
# 		print add

