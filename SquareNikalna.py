# Apko ek value di jayegi jese 10 toh apko 1-10 ke bich meh jitne bi number hai unke square ka sum 
# nikalna hai aur uske baad 1-10 ke bich jitne number hai uske sum karke joh value aye uska square nikalna hai aur
# dusri value meh se pheli value gatani hai.
# 1<sup>2</sup>+2<sup>2</sup>+3<sup>2</sup>+4<sup>2</sup>+.....+10<sup>2</sup> = 385
# (1+2+3+4+...+10)<sup>2</sup> = 3025
# 3025 - 385 = 2640


# day 2 task 5

user = int(raw_input("Entar number  "))
var = 1
squar = 0
add = 0
while var <= user:
	add = add+var
	squar=squar+var * var

	var+=1
Total = add * add
print Total - squar