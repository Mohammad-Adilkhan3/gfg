#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''

class Solution:
    # Return the kth smallest element in the given BST 
    def kthSmallest(self, root, k): 
        #code here.
        stack = []
        while True:
            while root:
                stack.append(root)  # Go left
                root = root.left
            if not stack:
                return -1  # If k is larger than the number of nodes
            root = stack.pop()  # Process node
            k -= 1
            if k == 0:
                return root.data  # Found kth smallest
            
            root = root.right
        
