class Solution:
    def startStation(self, gas, cost):
        # Your code here
        total_gas, total_cost, start, balance = 0, 0, 0, 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            balance += gas[i] - cost[i]
    
            # If balance goes negative, reset start station
            if balance < 0:
                start = i + 1
                balance = 0
    
        return start if total_gas >= total_cost else -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends