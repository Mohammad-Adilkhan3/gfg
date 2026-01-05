class Solution:
    def maxSubarraySum(self, Arr, K):
        # code here 
        N=len(Arr)
        cs = sum(Arr[:K])
        m = cs
        for i in range(K, N):
            cs = cs - Arr[i - K] + Arr[i]
            m = max(m, cs)
        return m
