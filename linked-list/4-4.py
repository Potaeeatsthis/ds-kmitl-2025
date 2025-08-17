class TextEditor() :
    def __init__(self) :
        self.text = []
        self.cursor = 0

    def process_commands(self, commands_str) :
        commands = commands_str.split(',')

        for i in commands :
            parts = i.split()
            command = parts[0]

            if command == 'I' and len(parts) > 1 :
                self.insert(parts[1])
            elif command == 'L' :
                self.left()
            elif command == 'R' :
                self.right()
            elif command == 'B' :
                self.backspace()
            elif command == 'D' :
                self.delete()

        self.display()

    def insert(self, word) :
        for i in word :
            self.text.insert(self.cursor, i)
            self.cursor += 1

    def display(self) :
        final_text = ''.join(self.text)

        output = list(final_text)

        output.insert(self.cursor, '|')

        print(''.join(output), end = ' ')

editor = TextEditor()

inp = input("Enter Input : ")
editor.process_commands(inp)

