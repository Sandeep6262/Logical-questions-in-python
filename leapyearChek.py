def leapyear(user):
	if user % 4 == 0 and user % 100 != 0:
		return "this is leap year"
	elif user%4==0 and user%100==0 and user%400==0:
		return "this is leap year"
	else:
		return "this is not leap year"

print leapyear(int(raw_input("Input any year  ")))