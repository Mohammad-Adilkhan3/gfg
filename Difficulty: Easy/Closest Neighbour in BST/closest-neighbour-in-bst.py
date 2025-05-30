'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def findMaxFork(self, root, k):
        #code here
        if root is None:
            return None
        
        greatest = -1
        current = root
        
        while current:
            if current.data <= k:
                greatest = current.data
                current = current.right
            else:
                current = current.left
                
        return greatest

        