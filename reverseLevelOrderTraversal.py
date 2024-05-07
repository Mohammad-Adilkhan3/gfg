class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def reverseLevelOrder(root):
    result = []
    if root is None:
        return result
    
    queue = []
    stack = []
    queue.append(root)
    
    while queue:
        node = queue.pop(0)
        stack.append(node.val)
        
        if node.right:
            queue.append(node.right)
        
        if node.left:
            queue.append(node.left)
    
    while stack:
        result.append(stack.pop())
    
    return result

# Example usage:
# Constructing Example 1:
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)

# Constructing Example 2:
root2 = TreeNode(10)
root2.left = TreeNode(20)
root2.right = TreeNode(30)
root2.left.left = TreeNode(40)
root2.left.right = TreeNode(60)

# Output Example 1:
print("Example 1:")
result1 = reverseLevelOrder(root1)
print(result1)

# Output Example 2:
print("Example 2:")
result2 = reverseLevelOrder(root2)
print(result2)
