class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None
        
def is_empty(head):
    return head is None

def print_linked_list(head):
    if is_empty(head):
        return ''
    
    nodes = []
    current_node = head

    while current_node:
        nodes.append(str(current_node.data))
        current_node = current_node.next

    return "->".join(nodes)

def print_reverse_linked_list(head):
    if is_empty(head):
        return ''
    
    nodes = []
    current_node = head

    while current_node:
        nodes.append(str(current_node.data))
        current_node = current_node.next

    return "->".join(nodes[::-1])

def append(head, new_data) :
    new_node = Node(new_data)
    
    if is_empty(head) :
        return new_node
    
    last = head
    
    while last.next :
        last = last.next

    last.next = new_node
    return head

def list_length(head) :
    length = 0 
    current_node = head
    
    while current_node :
        length += 1
        current_node = current_node.next

    return length

def insert(head, pos, new_data) :
    new_node = Node(new_data)

    if pos <= 0 :
        new_node.next = head
        return new_node

    current_node = head

    for _ in range(pos - 1) :
        if current_node.next is None :
            break
        current_node = current_node.next

    new_node.next = current_node.next
    current_node.next = new_node
    return head

def remove(head, key) :
    current_node = head
    
    if is_empty(head) :
        print("Not Found!")
        return head, False, -1
    
    if head.data == key :
        return head.next, True, 0

    current_node = head
    index = 0 
    
    while current_node.next and current_node.next.data != key :
        current_node = current_node.next
        index += 1
            
    if current_node.next :
        node_to_remove = current_node.next
        current_node.next = node_to_remove.next
        return head, True, index + 1
    else :
        return head, False, -1

def insert_head(head, new_data) :
    new_node = Node(new_data)
    new_node.next = head
    return new_node

inp = input("Enter Input : ").split(',')

head = None

for i in inp :
    command = i.split()
    
    if command[0] == "A" :
        head = append(head, command[1])
        print(f'linked list : {print_linked_list(head)}')
        print(f'reverse : {print_reverse_linked_list(head)}')

    elif command[0] == "I" :
        pos, new_data = command[1].split(':')

        if list_length(head) < int(pos) or int(pos) < 0 :
            print("Data cannot be added")
            print(f'linked list : {print_linked_list(head)}')
            print(f'reverse : {print_reverse_linked_list(head)}')
            continue

        else :
            head = insert(head, int(pos), new_data)
            print(f'index = {pos} and data = {new_data}')
            print(f'linked list : {print_linked_list(head)}')
            print(f'reverse : {print_reverse_linked_list(head)}')
        
    elif command[0] == "Ab" :
        head = insert_head(head, command[1])
        print(f'linked list : {print_linked_list(head)}')
        print(f'reverse : {print_reverse_linked_list(head)}')

    elif command[0] == "R" :
        head, bool, index = remove(head, command[1])
        
        if bool :
            print(f'removed : {command[1]} from index : {index}')
            
        print(f'linked list : {print_linked_list(head)}')
        print(f'reverse : {print_reverse_linked_list(head)}')