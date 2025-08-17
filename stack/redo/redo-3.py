inp = input("Enter Infix : ")
stack = []
res = ''

oper = ['+', '-', '*', '/', '^']

def prec(c) :
    if c == '+' or c == '-' :
        return 1

    elif c == '*' or c == '/' :
        return 2

    elif c == '^' :
        return 3

    else :
        return 0

for i in inp :
    if i.isalnum() :
        res += i

    elif i == '(' :
        stack.append(i)

    elif i == ')' :
        while stack and stack[-1] != '(' :
            res += stack.pop()
        stack.pop()

    else :
        while stack and prec(i) <= prec(stack[-1]) :
            res += stack.pop()
        stack.append(i)

while stack :
    res += stack.pop()

print(f"Postfix : {res}")
