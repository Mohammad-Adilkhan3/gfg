'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def bottomView(self, root):
        # code here
        if not root:
            return []
        hd_node = {}
        q = [(root, 0)]
        while q:
            node, hd = q.pop(0)  # Get front element
            hd_node[hd] = node.data
            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))
        result = [hd_node[hd] for hd in sorted(hd_node)]
        return result