user=int(raw_input(" input the number "))
All_divisibale=0
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
		# print factor_sum
		All_divisibale=All_divisibale+factor_sum 
print All_divisibale
	