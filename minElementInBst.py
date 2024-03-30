class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def min_in_bst(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.val

# Example usage:
# Create a BST
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(7)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(8)

# Find the minimum element
min_element = min_in_bst(root)
print("Minimum element in the BST:", min_element)
