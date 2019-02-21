magic_square = [
    [8, 3, 4],
    [1, 5, 9],
    [6, 7, 2]
]
print("Row")
print(magic_square[0][0]+magic_square[0][1]+magic_square[0][2])
print(magic_square[1][0]+magic_square[1][1]+magic_square[1][2])
print(magic_square[2][0]+magic_square[2][1]+magic_square[2][2])

print("colume")
print(magic_square[0][0]+magic_square[1][0]+magic_square[2][0])
print(magic_square[0][1]+magic_square[1][1]+magic_square[2][1])
print(magic_square[0][2]+magic_square[1][2]+magic_square[2][2])

print("diagonals")
print(magic_square[0][0]+magic_square[1][1]+magic_square[2][2])
print(magic_square[0][2]+magic_square[1][1]+magic_square[2][0])


# magic_square = [
#     [8, 3, 4],
#     [1, 5, 9],
#     [6, 7, 2]
# ]
# total = 0
# for i in magic_square:
# 	sum_1 = 0
# 	for j in i:
# 		sum_1+=j
# 	# print(sum_1)
# 	total+=sum_1

# if total % sum_1 == 0:
# 	m = True
# 	# print(m)
# 	m = sum_1


# sec_total = 0
# for y in range(len(magic_square)):
# 	add = 0
# 	for i in magic_square:
# 		for j in range(len(i)):
# 			if j == y:
# 				a=i[j]
# 				# print(a)
# 				add+=a
# 	# print(add)
# 	sec_total+=add
# # print(sec_total)
# # print(add)
# if sec_total%add==0:
# 	n = True
# 	# print(n)
# 	n=add

# ples=0
# add=0
# y=0
# o=2
# for i in magic_square:
# 	for j in range(len(i)):
# 		if j == y:
# 			b=i[y]
# 			y+=1
# 			# print(b)
# 			ples+=b
# 			break
# # print(ples)

# for i in magic_square:
# 	for j in range(len(i)):
# 		if j == o:
# 			c=i[o]
# 			add+=c
# 			o-=1
# 			# print(c)
# 			break
# # print(add) 

# if add==ples and add==m and m==n:
# 	print("magic_square hai")
# else:
# 	print("magic_square nahi hai")			
