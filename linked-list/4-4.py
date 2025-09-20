class TextEditor() :
    def __init__(self) :
        self.text = []
        self.cursor = 0

    def process_commands(self, commands_str) :
        commands = commands_str.split(',')

        for i in commands :
            parts = i.strip()
            command = parts[0]
            argument = None

            if len(parts) > 2 and parts[1] == ' ':
                argument = parts[2:]

            if command == 'I' and argument is not None:
                self.insert(argument)
            elif command == 'L' :
                self.left()
            elif command == 'R' :
                self.right()
            elif command == 'B' :
                self.backspace()
            elif command == 'D' :
                self.delete()

    def insert(self, word) :
        self.text.insert(self.cursor, word)
        self.cursor += 1

    def left(self) :
        if self.cursor > 0 :
            self.cursor -= 1

    def right(self) :
        if self.cursor < len(self.text) :
            self.cursor += 1

    def backspace(self) :
        if self.cursor > 0 :
            self.cursor -= 1
            self.text.pop(self.cursor)

    def delete(self) :
        if self.cursor < len(self.text) :
            self.text.pop(self.cursor)

    def display(self) :
        output_list = self.text[:]
        output_list.insert(self.cursor, '|')
        print(' '.join(output_list))

editor = TextEditor()

inp = input("Enter Input : ")
editor.process_commands(inp)
editor.display()
