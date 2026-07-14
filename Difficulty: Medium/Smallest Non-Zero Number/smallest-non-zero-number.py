class Solution:
    def find(self, arr):
        # code here
        ans = 0
        for val in reversed(arr):
            ans = (ans + val + 1) // 2
        return ans