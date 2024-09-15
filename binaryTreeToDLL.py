class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # This will act as the "prev" pointer in the DLL.
        self.right = None  # This will act as the "next" pointer in the DLL.

# Helper function to perform the conversion
def convertBTtoDLL(root):
    # Initialize previous and head pointers
    prev = None
    head = None

    # Define an inner recursive function for inorder traversal and linking
    def inorderConvert(current):
        nonlocal prev, head

        # Base case: if current node is None, return
        if current is None:
            return

        # Recursively convert the left subtree
        inorderConvert(current.left)

        # If prev is None, this is the leftmost node (i.e., the head of the DLL)
        if prev is None:
            head = current
        else:
            # Link the current node with the previous node
            current.left = prev
            prev.right = current

        # Move prev to the current node
        prev = current

        # Recursively convert the right subtree
        inorderConvert(current.right)

    # Call the recursive helper function
    inorderConvert(root)

    # Return the head of the DLL
    return head

# Function to print the DLL
def printDLL(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.right

# Example Usage:
# Let's create a binary tree
#       10
#      /  \
#     5   20
#    / \   / \
#   1   8 15  25

root = Node(10)
root.left = Node(5)
root.right = Node(20)
root.left.left = Node(1)
root.left.right = Node(8)
root.right.left = Node(15)
root.right.right = Node(25)

# Convert binary tree to doubly linked list
dll_head = convertBTtoDLL(root)

# Print the doubly linked list
print("Doubly Linked List:")
printDLL(dll_head)
