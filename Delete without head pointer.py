class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteNode(del_node):
    # Copy the value of the next node to the given node
    del_node.val = del_node.next.val
    
    # Delete the next node
    del_node.next = del_node.next.next

# Example usage:
# Create the linked list: 1 -> 2
node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

# Given node to delete: 1
del_node = node1
deleteNode(del_node)

# Print the remaining nodes
current = node1
while current:
    print(current.val, end=" ")
    current = current.next
# Output: 2
