#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        prev1, prev2 = cost[0], cost[1]  # Base cases
    
        for i in range(2, len(cost)):
            curr = cost[i] + min(prev1, prev2)
            prev1, prev2 = prev2, curr  # Shift forward
    
        return min(prev1, prev2)


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends