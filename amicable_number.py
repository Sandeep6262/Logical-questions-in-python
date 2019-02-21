user=int(raw_input(" input the number "))
for y in range(1,user):
	sum=0
	for i in range(1,y):
		if y%i==0:
			sum=sum+i
			# print sum

	factor_sum=0
	for j in range(1,sum):
		if sum%j==0:
			factor_sum=factor_sum+j
			# print n
	if factor_sum==y:
		print factor_sum 
	


# user=int(raw_input("enter the number "))
# sum=0
# for i in range(1,user):
# 	if user%i==0:
# 		sum=sum+i
# 		# print sum

# factor_sum=0
# for j in range(1,sum):
# 	if sum%j==0:
# 		factor_sum=factor_sum+j
# 		# print n

# if factor_sum==user:
# 	print "amicable number hai"
# else:
# 	print "amicable nhi hai"					
