numberDict = {"zero":0, "one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
# print numberDict["two"]


user = str(raw_input("Entar any string number you want sum   "))
var = user.split()
add = 0
for i in var:
	if i in numberDict:
		add = add+numberDict[i]

print add
