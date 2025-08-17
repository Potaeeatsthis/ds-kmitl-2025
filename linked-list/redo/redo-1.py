class Node() :
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

    if head is None :
        return new_node

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

    if current_node is None :
        return head

    previous_node.next = current_node.next
    current_node = None

    return head

def print_list(head) :
    nodes = []

    current_node = head

    while current_node :
        nodes.append(str(current_node.data))
        current_node = current_node.next

    print(" -> ".join(nodes) + " -> None")

inp = input("Enter Commands: ")

head = None

commands = inp.split()

i = 0

while i < len(commands) :
    command = commands[i]

    if command == "append" :
        head = append(head, commands[i + 1])

        i += 2

    elif command == "insert_head" :
        head = insert_head(head, commands[i + 1])

        i += 2

    elif command == "delete" :
        head = delete(head, commands[i + 1])

        i += 2

    elif command == "print" :
        print_list(head)

        i += 1
