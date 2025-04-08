#User function Template for python3
from collections import deque
class Solution:
    def firstNegInt(self, arr, k): 
        # code here 
        result = []
        q = deque()  # stores indices of negative numbers
    
        for i in range(len(arr)):
            # Add current element index if it's negative
            if arr[i] < 0:
                q.append(i)
            
            # Remove elements that are out of the current window
            if q and q[0] <= i - k:
                q.popleft()
            
            # Record the result once the window reaches size k
            if i >= k - 1:
                result.append(arr[q[0]] if q else 0)
    
        return result
                



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())

        if k <= 0 or k > len(arr):
            tc -= 1
            continue

        ob = Solution()
        ans = ob.firstNegInt(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends