inp = input()
stack = []
un_close = 0 

for i in range (len(inp)) :
	if inp[i] in "({[" :
		stack.append(inp[i])

	elif inp[i] in ")}]" :
		while stack and ((stack[-1] == '(' and inp[i] == ')') or (stack[-1] == '{' and inp[i] == '}') or (stack[-1] == '[' and inp[i] == ']')
			stack.pop()
		else :
			un_close += 1

un_open = len(stack)
