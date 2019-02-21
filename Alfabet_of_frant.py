import string
var = string.ascii_lowercase
capital = string.ascii_uppercase
bobels = ["a", "e", "i", "o", "u"]
user = str(raw_input("input alfabet "))
b = list(var)
y = list(capital)
string = ""
for j in user:
	if j == "z":
		string=string+"a"
	else:
		for i in range(len(b)):
			if j == b[i]:
				if b[i] in bobels:
					string = string+str(y[i])
				else:
					string = string+str(b[i+1])

print string
