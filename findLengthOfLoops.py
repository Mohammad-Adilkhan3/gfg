def countNodesinLoop(head):
    #Your code here
    slow = fast = head
    if head == None or head.next == None:
        return 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    if slow != fast:
        return 0
    slow = slow.next
    len = 1
    while slow != fast:
        len += 1
        slow = slow.next
    return len

