class Calculator :
    def __init__(self) :
        self.stack = []

    def run(self, instructions) :
        it = iter(instructions)

        for i in it :
            if i == "PSH" :
                value = int(next(it))
                self.stack.append(value)
                continue

            elif i == "POP" :
                if self.stack :
                    self.stack.pop()
                continue

            elif i == "DUP" :
                if self.stack :
                    self.stack.append(self.stack[-1])
                continue

            elif i in "+-*/" :
                a = self.stack.pop()
                b = self.stack.pop()

                if i == '+' :
                    self.stack.append(a + b)

                elif i == '-' :
                    self.stack.append(a - b)

                elif i == '*' :
                    self.stack.append(a * b)

                elif i == '/' :
                    self.stack.append(int(a / b))
                continue

            try :
                self.stack.append(int(i))
            except :
                print(f"Invalid instruction: {instruc}")
                return None

        if len(self.stack) == 1 :
            return self.stack[0]
        elif not self.stack :
            return 0
        else :
            return self.stack[-1]

print("* Stack Calculator *")
inp = input("Enter arguments : ").split()
calc = Calculator()
result = calc.run(inp)

if result is not None :
    print(result)
