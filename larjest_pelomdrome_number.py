polimdrom=0
for i in range(100,1000):
	for j in range(100,1000):
		b = str(i*j)
		# print(b)
		y=b[::-1]
		if y==b:
			if int(polimdrom) < int(b):
				polimdrom=b
print polimdrom