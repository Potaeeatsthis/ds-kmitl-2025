inp_str = input("Enter expresion : ")

stack = []
unmatched_close = 0

for i in inp_str :
    if i in "([{" :
        stack.append(i)

    elif i in ")]}" :
        if stack and ((stack[-1] == '(' and i == ')') or (stack[-1] == '{' and i == '}') or (stack[-1] == '[' and i == ']')) :
            stack.pop()
        else :
            unmatched_close += 1

unmatched_open = len(stack)

if unmatched_open == 0 and unmatched_close == 0:
    print(f"{inp_str} MATCH")
elif unmatched_open > 0 and unmatched_close > 0:
    print(f"{inp_str} Unmatch open-close")
elif unmatched_close > 0:
    print(f"{inp_str} close paren excess")
elif unmatched_open > 0:
    print(f"{inp_str} open paren excess   {unmatched_open} : {''.join(stack)}")
