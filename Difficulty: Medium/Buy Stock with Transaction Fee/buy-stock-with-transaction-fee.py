class Solution:
    def maxProfit(self, arr, k):
        # Code here
        hold, sold = float('-inf'), 0
        
        for p in arr:
            n_hold = max(hold, sold-p)
            n_sold = max(sold, hold+p-k)
            hold, sold = n_hold, n_sold
        
        return max(hold, sold)