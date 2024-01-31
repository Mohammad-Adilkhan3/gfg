def removeDuplicates(head):
    #code here
    current = head
    while current:
        next = current.next
        if next and current.data == next.data: 
            current.next = next.next
            current = current
        else:
            current = next
