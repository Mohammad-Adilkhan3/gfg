'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def countAllPaths(self, root, k):
        # code here
        def dfs(node, prefix_sum, prefix_sum_count, target, current_sum):
            nonlocal count
            if not node:
                return
    
            current_sum += node.data
            count += prefix_sum_count.get(current_sum - target, 0)
            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1
    
           
            dfs(node.left, prefix_sum, prefix_sum_count, target, current_sum)
            dfs(node.right, prefix_sum, prefix_sum_count, target, current_sum)
    
            
            prefix_sum_count[current_sum] -= 1
    
        count = 0
        prefix_sum_count = {0: 1}  # Initialize with 0 to handle paths starting from the root
        dfs(root, 0, prefix_sum_count, k, 0)
        
        return count % (10**9 + 7)