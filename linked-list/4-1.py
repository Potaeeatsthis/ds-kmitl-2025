class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

def append(head, new_data) :
    new_node = Node(new_data)

    if head is None :
        return new_node

    last = head

    while last.next :
        last = last.next

    last.next = new_node

    return head

def insert_head(head, new_data) :
    new_node = Node(new_data)

    new_node.next = head

    return new_node

def delete(head, key) :
    current_node = head

    if current_node and current_node.data == key :
        head = current_node.next
        current_node = None
        return head

    previous_node = None 
    while current_node and current_node.data != key :
        previous_node = current_node
        current_node = current_node.next

    previous_node.next = current_node.next
    current_node = None
    return head

def print_list(head) :
    output = []

    while head :
        output.append(str(head.data))
        head = head.next

    print(" -> ".join(output) + " -> None")

inp = input("Enter Commands: ")

head = None

commands = inp.split()

i = 0 

while i < len(commands) :
    command = commands[i]

    if command == "append" :
        new_data = commands[i + 1]
        head = append(head, new_data)

        i = i + 2

    elif command == "insert_head" :
        new_data = commands[i + 1]
        head = insert_head(head, new_data)

        i = i + 2

    elif command == "delete" :
        key = commands[i + 1] 
        head = delete(head, key)

        i = i + 2

    elif command == "print" :
        print_list(head)

        i = i + 1
