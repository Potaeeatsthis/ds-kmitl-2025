inp = input("Enter expresion : ")
stack = []
unmatched_close = 0

for char in range(len(inp)):
    if inp[char] in "([{":
        stack.append(inp[char])
    elif inp[char] in ")]}":
        if stack and ((stack[-1] == "(" and inp[char] == ")") or (stack[-1] == "[" and inp[char] == "]") or (stack[-1] == "{" and inp[char] == "}")):
            stack.pop()
        else:
            unmatched_close += 1

unmatched_open = len(stack)

if unmatched_open == 0 and unmatched_close == 0:
    print(f"{inp} MATCH")
elif unmatched_open > 0 and unmatched_close > 0:
    print(f"{inp} Unmatch open-close")
elif unmatched_close > 0:
    print(f"{inp} close paren excess")
elif unmatched_open > 0:
    print(f"{inp} open paren excess   {unmatched_open} : {''.join(stack)}")