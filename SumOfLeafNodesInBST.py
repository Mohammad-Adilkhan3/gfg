class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)

    if key < root.val:
        root.left = insert(root.left, key)
    elif key >= root.val:
        root.right = insert(root.right, key)

    return root

def sumOfLeafNodes(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.val

    return sumOfLeafNodes(root.left) + sumOfLeafNodes(root.right)

# Example usage:
arr1 = [67, 34, 82, 12, 45, 78]
root1 = None
for val in arr1:
    root1 = insert(root1, val)
print(sumOfLeafNodes(root1))  # Output: 135

arr2 = [45]
root2 = None
for val in arr2:
    root2 = insert(root2, val)
print(sumOfLeafNodes(root2))  # Output: 45
