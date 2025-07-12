inp = [int(i) for i in input("Enter All Bid : ").split()]

if len(inp) > 1 :
	max_inp = max(inp)
	inp.remove(max_inp)
	if max_inp in inp :
		print("error : have more than one highest bid")
	else :
		nd = max(inp)
		print(f"winner bid is {max_inp} need to pay {nd}")
