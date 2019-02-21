# qution 1
# 1
# 1 1
# 1 2 1
# 1 2 3 1
# 1 2 3 4 1
# 1 2 3 4 5 1

# user=int(raw_input("Input any number "))
# for i in range(user):
# 	a = i+1
	
# 	for j in range(1,a):
# 		print j,
# 	print 1



# Qution 2 kackrang

# 1 
# 1 2 1 
# 1 2 3 2 1 
# 1 2 3 4 3 2 1 
# 1 2 3 4 5 4 3 2 1 
# 1 2 3 4 5 6 5 4 3 2 1 
# 1 2 3 4 5 6 7 6 5 4 3 2 1 
# 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 


user = int(raw_input("Input any number  "))
for i in range(1,user):
	c=''
	for j in range(1,i+1):
		b=j
		c=str(b)+c
		print b,

	for k in range(1,len(c)):
		print c[k],
	print ''

