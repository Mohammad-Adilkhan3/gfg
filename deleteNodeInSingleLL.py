def __init__(self):
        self.data = None
        self.next = None
'''

def delNode(head, k):
    # Code here
    idx = 1
    x = k
    prev_node = None
    temp = head 
    while temp is not None:
        if idx == x:
            if temp == head:
                head = temp.next
            else:
                temp = prev_node 
                temp.next = temp.next.next


        idx +=1
        prev_node = temp
        temp = temp.next 
    
    return head
