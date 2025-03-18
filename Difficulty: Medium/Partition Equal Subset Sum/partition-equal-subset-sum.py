class Solution:
    def equalPartition(self, arr):
        # code here
        total_sum = sum(arr)
    
        # If the total sum is odd, partition is not possible
        if total_sum % 2 != 0:
            return False
        
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # A subset with sum 0 is always possible
    
        for num in arr:
            for j in range(target, num - 1, -1):  # Iterate backwards to avoid using same element multiple times
                dp[j] = dp[j] or dp[j - num]
    
        return dp[target]


#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends