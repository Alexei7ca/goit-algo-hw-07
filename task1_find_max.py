class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        elif key > node.val:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)

def find_max_value(root):
    if root is None:
        return None
    
    current = root
    while current.right is not None:
        current = current.right
    
    return current.val

if __name__ == '__main__':
    bst = BinarySearchTree()
    elements = [50, 30, 70, 20, 40, 60, 80]
    for element in elements:
        bst.insert(element)

    max_val = find_max_value(bst.root)
    
    print(f"Elements in the tree: {elements}")
    print(f"The maximum value in the BST is: {max_val}")