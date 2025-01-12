
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


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends