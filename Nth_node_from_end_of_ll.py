def length(head):
    count=0
    while head:
        count+=1
        head=head.next
    return count
def getNthFromLast(head,n):
    #code here
    temp=head
    if head is None or n>length(head):
        return -1
    for _ in range(length(head)-n):
        temp=temp.next
    return temp.data

