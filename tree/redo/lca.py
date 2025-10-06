class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        self.root = self._insert(self.root, data)
        return self.root

    def _insert(self, node, data):
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        elif data > node.data:
            node.right = self._insert(node.right, data)
        return node

    def height(self, node):
        if node is None:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def lca(self, data1, data2):
        current_node = self.root

        while current_node:
            if data1 > current_node.data and data2 > current_node.data:
                current_node = current_node.right
            elif data1 < current_node.data and data2 < current_node.data:
                current_node = current_node.left
            else:
                return current_node
        return None

T = BST()

try:
    inp = [int(i) for i in input("Enter Input : ").split()]
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
    inp = []

if inp:
    for i in inp:
        root = T.insert(i)

    if len(inp) >= 2:
        data1 = inp[0]
        data2 = inp[1]

        lca_node = T.lca(data1, data2)

        if lca_node:
            print(f"LCA of {data1} and {data2} is {lca_node.data}.")
        else:
            print("LCA Does Not Exist")

