def Anagram_fuction(user1,user2):
	if sorted(user1) == sorted(user2):
		print "Anagram hai"
	else:
		print "Anagram nahi hai"

	print sorted(user1)
	print sorted(user2)

Anagram_fuction(str(raw_input("input any word  ")),str(raw_input("input any word  ")))