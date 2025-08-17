inp = [str(i) for i in input("Enter Input : ")]

stack = []
num = 0

for i in range(len(inp)) :
    num += 1

    if inp[i] == '(' or inp[i] == '[' :
        stack.append(inp[i])

    else :
        if stack and ((stack[-1] == '(' and inp[i] == ')') or (stack[-1] == '[' and inp[i] == ']')) :
            stack.pop()
            num -= 2

if num == 0 :
    print(num, "\nPerfect ! ! !")
else :
    print(num)
