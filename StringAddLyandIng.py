# day 2 Task 2
user = str(raw_input("Entar any word  "))
if user[-2:] == "ly":
	print user
elif user[-3:] == "ing":
	print user+"ly"
else:
	print user+"ing"