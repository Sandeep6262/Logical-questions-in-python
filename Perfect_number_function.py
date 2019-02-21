def Perfect_number_function(user):
	var = 1
	while var <= user:
		add = 0
		num = 1
		while num < var:
			if var % num == 0:
				add = add + num

			num = num+1
		if add == var:
			print var

		var = var+1

Perfect_number_function(int(raw_input("input any number  ")))