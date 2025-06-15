class Solution:
    
    def smallestDivisor(self, arr, k):
        # Code here
        import math
        l ,r = 1, max(arr)
        while l<=r:
            mid = l + (r-l)//2
            count = 0
            for i in arr:
                count += math.ceil(i/mid)
                if count > k:
                    break
            if count <= k:
                r = mid - 1
            else:
                l = mid + 1
        return l