class Calculator:
    def __init__(self):
        self.stack = []

    def run(self, instructions):
        it = iter(instructions)
        for instruc in it:
            
            if instruc == "PSH" :
                value = int(next(it))
                self.stack.append(value)
                continue
            
            elif instruc == "DUP" :
                if self.stack :
                    self.stack.append(self.stack[-1])
                continue
            
            elif instruc == "POP" :
                if self.stack :
                    self.stack.pop()
                continue
            
            elif instruc in "+-*/" :
                a = self.stack.pop()
                b = self.stack.pop()
                if instruc == "+" :
                    self.stack.append(a + b)
                elif instruc == "-" :
                    self.stack.append(a - b)
                elif instruc == "*" :
                    self.stack.append(a * b)
                elif instruc == "/" :
                    self.stack.append(int(a / b))
                continue

            try :
                self.stack.append(int(instruc))
            except ValueError:
                print(f"Invalid instruction: {instruc}")
                return None
        
        if len(self.stack) == 1:
            return self.stack[0]
        elif not self.stack :
            return 0
        else :
            return self.stack[-1]

print("* Stack Calculator *")
input = input("Enter arguments : ").split()
calc = Calculator()
result = calc.run(input)
if result is not None:
    print(result)
