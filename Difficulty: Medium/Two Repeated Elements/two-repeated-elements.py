#User function Template for python3

class Solution:
    from collections import Counter
    #Function to find two repeated elements.
    def twoRepeated(self, n, arr):
        #Your code here
        res=[]
        s=set()
        for i in arr:
            if i not in s:
                s.add(i)
            else:
                res.append(i)
        return res[0],res[1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        ans = obj.twoRepeated(n, arr)
        print(ans[0], ans[1])

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends