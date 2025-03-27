#User function Template for python3

class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr.sort()
        dep.sort()
        
        n = len(arr)
        platforms = 0
        max_platforms = 0
        i, j = 0, 0
    
        while i < n and j < n:
            if arr[i] <= dep[j]:  # A train arrives
                platforms += 1
                max_platforms = max(max_platforms, platforms)
                i += 1
            else:  # A train departs
                platforms -= 1
                j += 1
    
        return max_platforms


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends