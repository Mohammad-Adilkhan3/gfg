class Solution:
    def minSoldiers(self, arr, k):
        # code here
        import math
        arr.sort(key=lambda item:k-(item%k) if item%k else 0)
        n=len(arr)
        ans=0
        for i in range(math.ceil(n/2)):
            if arr[i]%k:
                ans+=(k-arr[i]%k)
        return ans