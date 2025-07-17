'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''


class Solution:
    def splitList(self, head):
        #code here
        if not head or not head.next: return head
        fast=head.next
        slow=head
        while fast!=head and fast.next!=head:
            slow=slow.next
            fast=fast.next.next
        t=slow.next
        slow.next=head
        fast=t
        while fast.next!=head:fast=fast.next
        
        fast.next=t
        
        return [head,t]
        