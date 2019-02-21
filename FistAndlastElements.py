# day 2 Task 1
# Apko ek string di jayegi jahan apko string ke phele 2 aur akhir ke 2 letters 
# print karwana hai lekin agar woh string meh 2 se kaam letters hai toh kuch bi nhi print hoga.



user = str(raw_input("Entar word  "))
if int(len(user)) > 1:
	print user[0]+user[1]+user[-2]+user[-1]



# user = str(raw_input("Entar word  "))
# user1 = int(len(user))
# a = user1-2
# b = user1-1
# if user1 > 1:
# 	string = ''
# 	for i in range (user1):
# 		if i == 0 or i == 1:
# 			string=string+user[i]
# 	for j in range (user1):
# 		if j == a or j == b:
# 			string=string+user[j]

# 	print string



