# Anagram words joh kuch letter ke position ko re-arrange karke bante ha jishme koi bi letter repeat nhi hota.
# Jese pears and spare yeh dono ek dusre ke Anagram kyunki yahan ek bi letter repeat nhi kiya gyaa hai jesa app dekh sakte hai.
# Jese pears and spares yeh dono ek dusre ke Anagram nhi hai kyunki yahan s 2 bar repeat kiya gyaa hai jesa app dekh sakte hai.


# Anagram words  program
user = raw_input("Entar word 1 ")
user1 = raw_input("Entar word 2  ")

if sorted(user) == sorted(user1):
	print "Anagram hai"
else:
	print "Anagram nahi hai"