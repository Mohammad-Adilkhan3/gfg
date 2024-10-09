class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

def construct_2D_linked_list(matrix):
    if not matrix:
        return None

    n = len(matrix)    # Number of rows
    m = len(matrix[0]) # Number of columns

    # To store the head of the 2D linked list
    head = None

    # To store the head nodes of the previous row
    prev_row = [None] * m

    # Traversing the matrix
    for i in range(n):
        prev_node = None  # To store the previous node in the same row
        for j in range(m):
            # Create a new node for matrix[i][j]
            new_node = Node(matrix[i][j])
            
            # Set the head to the first node
            if i == 0 and j == 0:
                head = new_node
            
            # Link the node horizontally (right pointer)
            if prev_node:
                prev_node.right = new_node

            # Link the node vertically (down pointer)
            if i > 0:
                prev_row[j].down = new_node

            # Update the prev_node to the current node for the next iteration in the row
            prev_node = new_node

            # Update the prev_row for vertical linking in the next row
            prev_row[j] = new_node

    return head

