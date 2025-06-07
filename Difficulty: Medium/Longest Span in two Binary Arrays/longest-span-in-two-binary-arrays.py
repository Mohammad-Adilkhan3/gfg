class Solution:
    def longestCommonSum(self, a1, a2):
        #Code here.
        n = len(a1)
        diff_map = {}
        max_len = 0
        curr_sum = 0
    
        for i in range(n):
            diff = a1[i] - a2[i]
            curr_sum += diff
    
            if curr_sum == 0:
                max_len = i + 1
            elif curr_sum in diff_map:
                max_len = max(max_len, i - diff_map[curr_sum])
            else:
                diff_map[curr_sum] = i
    
        return max_len
            
            