'''
class Node:
    def __init__(self, val):
        self.data=val
        self.left=None
        self.right=None
'''
class Solution:
    def sumOfLongRootToLeafPath(self, root):
        #code here
        def dfs(node):
            if not node:
                return (0, 0)  # (length, sum)
            
            left_len, left_sum = dfs(node.left)
            right_len, right_sum = dfs(node.right)
            
            if left_len > right_len:
                return (left_len + 1, left_sum + node.data)
            elif right_len > left_len:
                return (right_len + 1, right_sum + node.data)
            else:
                return (left_len + 1, max(left_sum, right_sum) + node.data)
        
        _, max_sum = dfs(root)
        return max_sum