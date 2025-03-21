class Solution:  
    def findMaxSum(self,arr):
        # code here
        n = len(arr)
        if n == 1:
            return arr[0]
    
        # DP Table
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
    
        for i in range(2, n):
            dp[i] = max(dp[i-1], arr[i] + dp[i-2])
    
        return dp[-1]


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends