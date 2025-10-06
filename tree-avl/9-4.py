import math

class AVLNode:
    """A node in an AVL Tree."""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """An AVL Tree with a top-down visual printing method."""

    # --- Core AVL Logic (Correct and Unchanged) ---
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def rotateRight(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rotateLeft(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    
    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
        return self.getMinValueNode(root.left)

    def insert(self, root, data):
        if not root:
            return AVLNode(data)
        elif data < root.data:
            root.left = self.insert(root.left, data)
        else:
            root.right = self.insert(root.right, data)

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and data < root.left.data:
            return self.rotateRight(root)
        if balance < -1 and data > root.right.data:
            return self.rotateLeft(root)
        if balance > 1 and data > root.left.data:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and data < root.right.data:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        return root

    def delete(self, root, data):
        if not root:
            return root
        elif data < root.data:
            root.left = self.delete(root.left, data)
        elif data > root.data:
            root.right = self.delete(root.right, data)
        else:
            if root.left is None: return root.right
            elif root.right is None: return root.left
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)
        
        if root is None: return root

        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        balance = self.getBalance(root)

        if balance > 1 and self.getBalance(root.left) >= 0: return self.rotateRight(root)
        if balance < -1 and self.getBalance(root.right) <= 0: return self.rotateLeft(root)
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)
        return root

    # --- New and Improved Printing Logic ---
    def printTree(self, root):
        """Prints the tree in a top-down, visually intuitive format."""
        if not root:
            # Handle empty tree case after a deletion
            # print("Tree is empty.") # Optional: uncomment if you want a message
            return
        
        height = self.getHeight(root)
        # Calculate the width needed for the bottom level of the tree
        width = (2 ** height) * 4 
        
        # Create a grid (list of lists) to store the display characters
        output = [[' ' for _ in range(width)] for _ in range(height)]
        
        # Recursively fill the grid
        self._fill_grid(root, output, 0, 0, width)
        
        # Print each line of the grid
        for line in output:
            print("".join(line))

    def _fill_grid(self, node, output, level, left, right):
        """Recursively fills the output grid to prepare for printing."""
        if not node:
            return
        
        # Position the current node in the middle of its allowed space
        mid = (left + right) // 2
        output[level][mid] = str(node.data)
        
        # Recursively call for left and right children
        self._fill_grid(node.left, output, level + 1, left, mid - 1)
        self._fill_grid(node.right, output, level + 1, mid + 1, right)

# --- Main Program Execution ---
print("*** AVL Tree ***")
numbers_str = input("Enter numbers to insert: ").split()
numbers = [int(n) for n in numbers_str]

tree = AVLTree()
root = None

# Insertion Phase
for num in numbers:
    root = tree.insert(root, num)
    tree.printTree(root)
    print("------------------------------")

# Deletion Phase
while root is not None:
    # Continuously delete the current root
    root = tree.delete(root, root.data)
    tree.printTree(root)
    if root is not None:
         print("------------------------------")

print("===== End of program =====")
