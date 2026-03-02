class Solution:
    def maxWater(self, arr):
        # code here
        total_water = 0
        lmax, rmax = 0, 0
        i, j = 0, len(arr) - 1
        
        while i < j:
            lmax = max(lmax, arr[i])
            rmax = max(rmax, arr[j])
            
            if arr[i] <= arr[j]:
                total_water += lmax - arr[i]
                i += 1
            else:
                total_water += rmax - arr[j]
                j -= 1
        
        return total_water