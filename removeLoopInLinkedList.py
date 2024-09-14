class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeLoop(head):
    if not head or not head.next:
        return head
    
    slow = head
    fast = head
    
    # Step 1: Detect if there's a loop using Floyd's Cycle Detection
    has_loop = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_loop = True
            break
    
    # If there is no loop, return the list as it is
    if not has_loop:
        return head
    
    # Step 2: Find the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next
    
    # Step 3: Remove the loop by finding the node before the start of the loop
    loop_start = slow
    ptr = loop_start
    while ptr.next != loop_start:
        ptr = ptr.next
    ptr.next = None  # Break the loop
    
    return head

# Function to create a linked list from a list and create a loop at position 'pos'
def createLinkedList(arr, pos):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    loop_node = None
    if pos == 0:
        loop_node = None
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
        if i == pos - 1:  # pos is 1-based index
            loop_node = current
    if loop_node:
        current.next = loop_node
    return head

# Function to check if the linked list has a loop
def hasLoop(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# Driver code for testing
arr1 = [1, 3, 4]
pos1 = 2  # Create a loop at position 2 (1-based)
head1 = createLinkedList(arr1, pos1)
removeLoop(head1)
print(not hasLoop(head1))  # Output: True

arr2 = [1, 8, 3, 4]
pos2 = 0  # No loop
head2 = createLinkedList(arr2, pos2)
removeLoop(head2)
print(not hasLoop(head2))  # Output: True

arr3 = [1, 2, 3, 4]
pos3 = 1  # Create a loop at position 1 (1-based)
head3 = createLinkedList(arr3, pos3)
removeLoop(head3)
print(not hasLoop(head3))  # Output: True
