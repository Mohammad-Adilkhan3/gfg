
class Solution:
    def maxWater(self, arr):
        # code here
        i,j=0,len(arr)-1
        res=0
        while i<j:
            h=min(arr[i],arr[j])
            b=j-i
            res=max(res,h*b)
            if arr[i]<arr[j]:
                i+=1
            else:
                j-=1
        return res
            


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