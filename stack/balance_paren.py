inp = input("Enter Input : ")
stack = []
is_balance = True

for i in inp :
    if i in "({[" :
        stack.append(i)

    elif i in ")}]" :
        if not stack or not ((stack [-1] == '(' and i == ')') or (stack[-1] == '{' and i == '}') or (stack[-1] == '[' and i == ']')) :
            is_balance = False
            break
        else :
            stack.pop()

if is_balance and not stack :
    print("True")
else :
    print("False")
