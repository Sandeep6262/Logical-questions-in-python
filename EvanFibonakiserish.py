# Apko ek postion di jayegi jish position tak ke sare Fibonacci series meh se jitne 
# bi even number wale ha element hai uneh print karwana hai apko.


# Fibonacci serises
user = int(raw_input("Entar number  "))
fist = 0
second = 1
thard = 0
var = 0
while var < user:
	if thard % 2 == 0:
		print thard

	thard = fist+second
	fist = second
	second = thard
	
	var+=1