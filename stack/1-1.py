inp = input("Enter Input : ")
stack = []
num = 0

for char in range(len(inp)):
	num += 1
	if inp[char] == "("  or inp[char] == "[" :
		stack.append(inp[char])

	else :
		if stack and ((stack[-1] == "(" and inp[char] == ")") or (stack[-1] == "[" and inp[char] == "]")):
			stack.pop()
			num -= 2
   
if num == 0 :
    print(num, "\nPerfect ! ! !")
else :
    print(num)