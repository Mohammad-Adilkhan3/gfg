# class Node:
#     def __init__(self, val):
#         self.data = val
#         self.left = None
#         self.right = None

# return the Kth largest element in the given BST rooted at 'root'
class Solution:
    def kthLargest(self,root, k):
        #your code here
        l=[]
        def inord(root,l):
            if not root: return root
            inord(root.left,l)
            l.append(root.data)
            inord(root.right,l)
            return l
        res=inord(root,l)
        return res[-k]