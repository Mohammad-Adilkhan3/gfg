class Solution:
    def findKRotation(self, arr):
        # code here
        n=len(arr)
        if arr==sorted(arr):return 0
        for i in range(n):
            if arr[i]>arr[i+1]:return i+1
        