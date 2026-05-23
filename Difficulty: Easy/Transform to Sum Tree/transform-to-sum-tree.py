''' Structure for Tree Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

'''
class Solution:
    def toSumTree(self, root):
        # code here
        if not root:return 0
        l=self.toSumTree(root.left)
        r=self.toSumTree(root.right)
        temp=root.data
        root.data=l+r
        return root.data+temp