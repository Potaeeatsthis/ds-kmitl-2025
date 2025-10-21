class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        self.height = 1

    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def search(self, node, key):
        if not node or node.data == key:
            return node
        return self.search(node.left if key < node.data else node.right, key)

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def left_rotate(self, node):
        new_root = node.right
        node.right = new_root.left
        new_root.left = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def right_rotate(self, node):
        new_root = node.left
        node.left = new_root.right
        new_root.right = node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def insert_node(self, node, key):
        if not node:
            return Node(key)
        if key < node.data:
            node.left = self.insert_node(node.left, key)
        elif key > node.data:
            node.right = self.insert_node(node.right, key)
        else:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and key < node.left.data:
            return self.right_rotate(node)
        if balance < -1 and key > node.right.data:
            return self.left_rotate(node)
        if balance > 1 and key > node.left.data:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and key < node.right.data:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def get_min_value_node(self, node):
        while node and node.left:
            node = node.left
        return node

    def delete_node(self, node, key):
        if not node:
            return node
        if key < node.data:
            node.left = self.delete_node(node.left, key)
        elif key > node.data:
            node.right = self.delete_node(node.right, key)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left
            temp = self.get_min_value_node(node.right)
            node.data = temp.data
            node.right = self.delete_node(node.right, temp.data)

        if not node:
            return node

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        balance = self.get_balance(node)

        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.left_rotate(node)
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.left_rotate(node.left)
            return self.right_rotate(node)
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.right_rotate(node.right)
            return self.left_rotate(node)
        return node

    def delete_root(self):
        if not self.root:
            return None
        root_value = self.root.data
        self.root = self.delete_node(self.root, root_value)
        return self.root

def get_tree_height(node):
    if not node:
        return 0
    return 1 + max(get_tree_height(node.left), get_tree_height(node.right))

def print_levels(root):
    if not root:
        print("   0    ")
        return

    height = get_tree_height(root)
    queue = [(root, 0)]
    current_level = 0
    level_nodes = []

    while queue:
        node, level = queue.pop(0)

        if level != current_level:
            if level_nodes:
                _print_level(level_nodes, current_level, height)
            level_nodes = []
            current_level = level

        level_nodes.append(node)

        if level < height - 1:
            if node:
                queue.append((node.left, level + 1))
                queue.append((node.right, level + 1))
            else:
                queue.append((None, level + 1))
                queue.append((None, level + 1))

    if level_nodes:
        _print_level(level_nodes, current_level, height)

def _print_level(nodes, level, total_height):
    while nodes and nodes[-1] is None:
        nodes.pop()

    if not nodes:
        return

    # Spacing based on tree height and level
    if total_height == 1:
        spaces_before = 3
        spaces_between = 0
    elif total_height == 2:
        if level == 0:
            spaces_before = 7
            spaces_between = 0
        else:
            spaces_before = 3
            spaces_between = 7
    elif total_height == 3:
        if level == 0:
            spaces_before = 15
            spaces_between = 0
        elif level == 1:
            spaces_before = 7
            spaces_between = 15
        else:
            spaces_before = 3
            spaces_between = 7
    elif total_height == 4:
        if level == 0:  # height 1
            spaces_before = 31
            spaces_between = 0
        elif level == 1:  # height 2
            spaces_before = 15
            spaces_between = 31
        elif level == 2:  # height 3
            spaces_before = 7
            spaces_between = 15
        else:  # level == 3, height 4
            spaces_before = 3
            spaces_between = 7
    else:  # total_height > 4
        if level == 0:
            spaces_before = 2 ** (total_height + 1) - 1
            spaces_between = 0
        else:
            spaces_before = 2 ** (total_height - level) - 1
            spaces_between = 2 ** (total_height - level + 1) - 1

    line_parts = []
    if spaces_before > 0:
        line_parts.append(" " * spaces_before)
    for i, node in enumerate(nodes):
        if node is not None:


            if node is not None:
                
                line_parts.append(str(node.data))
                line_parts.append(" " * (spaces_between-(len(str(node.data))-1)))
            
            else:
                line_parts.append(" ")

    print("".join(line_parts))

tree = AVL()
print(' *** AVL Tree ***')
data = input("Enter numbers to insert: ").split()

for num in data:
    tree.root = tree.insert_node(tree.root, int(num))

print_levels(tree.root)
print("------------------------------")

while tree.root:
    tree.delete_root()
    if tree.root:
        print_levels(tree.root)
        print("------------------------------")

print("===== End of program =====")
