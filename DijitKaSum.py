# Apko ek number diya jayega aur apko ush number ke digit ka sum nikalna hai.
# Jese 2345 diya gaya hai apko toh iska sum hoga 2+3+4+5=14.



user = str(raw_input("Entar numbear you want sum  "))
add = 0
for i in user:
	add = add+ int(i)
print add


# user = str(raw_input("Entar numbear you want sum  "))
# var = 0
# sum1 = 0
# while var < len(user):
# 	sum1 = sum1 + int(user[var])

# 	var+=1

# print sum1