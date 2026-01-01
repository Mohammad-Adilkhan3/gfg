'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        def length(head):
            curr = head
            ans = 0
            while curr:
                ans += 1
                curr = curr.next
            return ans
        
        l1,l2 = length(head1),length(head2)
        
        if l1>l2:
            for _ in range(l1-l2):
                head1 = head1.next
        else:
            for _ in range(l2-l1):
                head2 = head2.next
        
        while(head1 != head2):
            head1 = head1.next
            head2 = head2.next
        
        return head1