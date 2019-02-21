user = int(raw_input("input any number "))		
add = 0
prime = 0
num = 2
anliminted=3
# number=1
while num < anliminted:
	if user == add:
		print prime
		break
	
	var = 2
	while var < num:
		if num % var == 0:
			break

		var+=1
	else:
		add+=1
		prime = num
		# print number,prime
		# number+=1

	num+=1
	anliminted+=1