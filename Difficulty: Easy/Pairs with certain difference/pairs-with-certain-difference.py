class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        n = len(arr)
        
        arr.sort(reverse = True)
        total = 0
        skipNext = False
        
        for i in range(n - 1):
            if skipNext:
                skipNext = False
                continue
            
            if arr[i] - arr[i + 1] < k:
                total += arr[i] + arr[i + 1]
                skipNext = True
        
        return total