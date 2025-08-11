class Node :
    def __init__(self, data):
        self.data = data
        self.next = None

def create_list(strings) :
    if not strings :
        return None
    
    dummy_node = Node(0)
    current_node = dummy_node
    
    data = strings.split(',')

    for item in data :
        current_node.next = Node(int(item))
        current_node = current_node.next

    return dummy_node.next

def print_linked_list(head):
    if head is None :
        return None
    
    nodes = []
    current_node = head
    
    while current_node :
        nodes.append(str(current_node.data))
        current_node = current_node.next

    return " ".join(nodes)

def merge_sorted_lists(head1 ,head2) :
    dummy_node = Node(0)
    tail = dummy_node

    while head1 and head2 :        
        if head1.data < head2.data :
            tail.next = head1
            head1 = head1.next
        else :
            tail.next = head2
            head2 = head2.next
        tail = tail.next

    if head1 :
        tail.next = head1
    elif head2 :
        tail.next = head2

    return dummy_node.next

head1 = None
head2 = None

head1, head2 = input("Enter 2 Lists : ").split(' ')

head1 = create_list(head1)
head2 = create_list(head2)

print("LL1 :", print_linked_list(head1))
print("LL2 :", print_linked_list(head2))
print("Merge Result :", print_linked_list(merge_sorted_lists(head1, head2)))