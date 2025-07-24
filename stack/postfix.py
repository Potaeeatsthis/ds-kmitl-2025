inp = input("Enter Postfix : ")
stack = []
operators = ['+', '-', '*', '/']

def prec(c) :
    if c == '+' or c == '-' :
        return 1
    elif c == '*' or c == '/' :
        return 2
    else :
        return 0

for i in inp :
    if i.isnumeric() :
        stack.append(int(i))

    elif i in operators :
        b = stack.pop()
        a = stack.pop()

        if i == '+' :
            stack.append(a + b)

        elif i == '-' :
            stack.append(a - b)

        elif i == '*' :
            stack.append(a * b)

        elif i == '/' :
            stack.append(a / b)

print(f"Result : {stack}")

