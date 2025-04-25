#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        from collections import Counter
        n=len(arr)//2
        c=Counter(arr)
        for i in c:
            if c[i]>n:
                return i
        return -1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends