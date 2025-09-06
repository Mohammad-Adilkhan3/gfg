#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    # Function to find the length of a loop in the linked list.
    def lengthOfLoop(self, head):
        #code here
        if head is None or head.next is None:
            return 0
        slow = head.next
        fast = head.next.next
        
        while fast is not None and fast.next is not None :
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
            
        l=1
        if fast is None or fast.next is None:
            return 0
        t=slow.next
        # t = t.next
        while(t!=slow):
            t=t.next
            l+=1
        return l


