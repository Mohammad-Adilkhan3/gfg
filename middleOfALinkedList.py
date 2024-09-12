def findMiddle(head: ListNode) -> ListNode:
    # Initialize both slow and fast pointers to the head of the list
    slow = head
    fast = head
    
    # Traverse the list with slow and fast pointers
    while fast and fast.next:
        slow = slow.next         # Move slow pointer by 1 step
        fast = fast.next.next    # Move fast pointer by 2 steps
    
    # When fast pointer reaches the end, slow pointer will be at the middle
    return slow
