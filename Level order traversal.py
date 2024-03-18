class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    if not root:
        return []
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize a queue to perform level order traversal
    queue = []
    queue.append(root)
    
    # Perform level order traversal
    while queue:
        # Dequeue the front node
        node = queue.pop(0)
        
        # Process the dequeued node
        result.append(node.val)
        
        # Enqueue left and right children if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

# Example usage:
# Create the binary tree for example 1
root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(2)

# Perform level order traversal
print(levelOrder(root1))  # Output: [1, 3, 2]

# Create the binary tree for example 2
root2 = TreeNode(10)
root2.left = TreeNode(20)
root2.right = TreeNode(30)
root2.left.left = TreeNode(40)
root2.left.right = TreeNode(60)

# Perform level order traversal
print(levelOrder(root2))  # Output: [10, 20, 30, 40, 60]
