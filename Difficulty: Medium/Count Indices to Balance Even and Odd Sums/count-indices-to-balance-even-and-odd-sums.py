class Solution:
    def cntWays(self, arr):
        # code here
        n = len(arr)
        suffix_diff = sum(arr[:n:2]) - sum(arr[1:n:2])
        prefix_diff = count = 0
        for i, a in enumerate(arr):
            if i & 1:
                suffix_diff += a
                count += prefix_diff == suffix_diff
                prefix_diff -= a
            else:
                suffix_diff -= a
                count += prefix_diff == suffix_diff
                prefix_diff += a
        return count