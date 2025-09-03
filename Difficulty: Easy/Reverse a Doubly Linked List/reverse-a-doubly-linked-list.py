#User function Template for python3

'''
class Node: 
    def __init__(self, data): 
        self.data = data  
        self.next = None
        self.prev = None
'''

class Solution:
    def reverse(self, head):
        if not head:
            return None
        
        current = head
        new_head = None
        
        while current:
            current.next, current.prev = current.prev, current.next
            new_head = current
            current = current.prev
        return new_head



